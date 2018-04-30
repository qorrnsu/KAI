from textblob.classifiers import NaiveBayesClassifier
from glob import glob
import random, json, pickle
# from pprint import pprint

class IntentClassifier:
    """
    This intent classifier is a Python interface that uses NaiveBayesClassifier from textblob.  
    It trains data from local data folder that contains json data files,
    which each has a name, training phrases(list), desired responses(list).
    Test file are located in the test folder as json format that has phrases and each 
    corresponding intent. Trained classifier can be saved or loaded, methods are 
    implemented using pickling.
    """
    def __init__(self):
        """Construtor of the intent classifier"""
        self._responses = {}

    def __load_data(self):
        """Load data from the local 'data' folder that contains json data files for training"""
        print("loading training data...")
        training_data = []
        files = glob('data/*.json')
        for file in files:
            print("loading", file)
            with open(file) as data_file:
                training_data.append(json.load(data_file))
        return training_data

    def __load_test(self):
        """Load data from the local 'test' folder that contains json data files for testing"""
        print("loading testing data...")
        with open('test/test.json') as test_file:
            return json.load(test_file)

    def __build_responses(self, intents):
        """Create dictionary of intent mapping each to lists of responses"""
        responses = {}
        for intent in intents:
            responses[intent['name']] = intent['responses']
        return responses

    def __arrange_data(self, intents):
        """Convert a json lists to a list of tuples each contains utterance and intent"""
        return [(utterance, intent['name']) for intent in intents for utterance in intent['userSays']]

    def __arrange_test(self, tests):
        """Convert a json to a list of tuples each containts phrase and intent"""
        return [(test['utterance'], test['intent']) for test in tests['tests']]

    def train(self, utterances=[]):
        """
        Loads data from local data folder that contains json data files to train the Naive Bayes Classifier
        and populate a dictionary of intents mapping to each list of responses if no utterances list were given

        Keyword Arguments: 
        intents -- is a list containing tuples of phrase and intent to train (optional)
        """
        if not utterances:
            json_data = self.__load_data()
            self._responses = self.__build_responses(json_data)
            utterances = self.__arrange_data(json_data)
        self._cl = NaiveBayesClassifier(utterances)

    def update(self, utterances=[]):
        """
        Loads data from local data folder that contains json data files to train the Naive Bayes Classifier
        and populate a dictionary of intents mapping to each list of responses if no utterances list were given

        Keyword Arguments: 
        intents -- is a list containing tuples of phrase and intent to train (optional)
        """
        if not utterances:
            json_data = self.__load_data()
            self._responses = {**self._responses, **self.__build_responses(utterances)}
            utterances = self.__arrange_data(json_data)
        self._cl.update(utterances)

    def test(self):
        """Test the accuracy of the classifier"""
        data_set = self.__arrange_test(self.__load_test())
        return self._cl.accuracy(data_set)

    def classify(self, target):
        """Classify a text"""
        label = self._cl.classify(target)
        return label

    def getProbability(self, target, intent):
        """Get probability of a phrase to an intent"""
        guess = self._cl.prob_classify(target)
        return round(guess.prob(intent), 2)

    def response(self, target):
        """Get a response according to the intent of the text"""
        responses = self._responses[self.classify(target)]
        return random.choice(responses)
    
    def addResponse(self, text, intent):
        """Add a response to the dictionary"""
        self._responses[intent].append(text)

    def addResponses(self, utterances):
        """Add list of tuples each containing response and intent to responses"""
        for utterance in utterances:
            self._responses[utterance[1]].append(utterance[0])

    def save(self, path):
        """Save the current trained classifier"""
        with open(path, "wb") as classifier_f:
            pickle.dump(self, classifier_f)

    def load(path):
        """A class method that load from local classifier"""
        with open(path, "rb") as classifier_f:
            classifier = pickle.load(classifier_f)
        return classifier



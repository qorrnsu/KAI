import translator, recognizer, tts, time, vlc
from intent_recognition import IntentClassifier
from weather_korea import ask_weather

# Create classifier
classifier = IntentClassifier()

# Features
features = {'weather': ask_weather}

def play_file():
    p = vlc.MediaPlayer("output.mp3")
    p.play()
    time.sleep(1)
    while p.is_playing():
        time.sleep(1)

def trainAI():
    classifier.train()
    classifier.save("k_classifier.pickle")
    print(classifier.test())
    print('Trained classifier')

def testAI():
    while True:
        text = input("Test utterance: ")
        print(classifier.classify(text))


def main():
    classifier = IntentClassifier.load("k_classifier.pickle")

    while True:
        # Ask
        tts.speak("무엇을 도와 드릴까요?")
        play_file()

        # Listen
        sentence = recognizer.recognize()
        if sentence[0]:
            # answer = dialogflow.ask(sentence[1])
            confidence = classifier.getProbability(
                sentence[1], classifier.classify(sentence[1]))
            intention = classifier.classify(sentence[1])

            # FEATURES
            if intention in features:
                answer = features[intention]()
            # CONVERSATION
            elif confidence > 0.21: # confidence boundary
                response = classifier.response(sentence[1])
                answer = response
            # NO ANSWER
            else:
                answer = "잘 모르겠어요"

            if(tts.speak(answer)):
                play_file()
        else:
            if(tts.speak(sentence[1])):
                play_file()

    # translated = translator.translate(sentence)['message']['result']['translatedText']
    # print('Translation: %s' % translated) #DEBUG

if __name__ == "__main__":
    trainAI()
    # testAI()
    main()

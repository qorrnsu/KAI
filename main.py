####################
# HOTWORD DETECTOR #
####################
import snowboydecoder, signal

interrupted = False
sensitivity = 0.6
model = 'KAIVA.pmdl'
detector = snowboydecoder.HotwordDetector(model, sensitivity=sensitivity)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def listen():
    print("Standby...")
    signal.signal(signal.SIGINT, signal_handler) # capture SIGINT signal, e.g., Ctrl+C
    detector.start(detected_callback=main,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

####################
#  CORE FUNCTIONS  #
####################
import sys, translator, recognizer, tts, time, vlc
from weather_korea import ask_weather
from intent_recognition import IntentClassifier

classifier = IntentClassifier()
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

def loadAI():
    classifier = IntentClassifier.load("k_classifier.pickle")

def main():
    # Turn off hotword detector
    detector.terminate()

    # Ask
    tts.speak("네! 주인님")
    play_file()

    # Listen
    print("Listening...")
    sentence = recognizer.recognize()

    # Processing
    print("Processing...")
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

    # Turn back on hotword detector
    listen()

    # translated = translator.translate(sentence)['message']['result']['translatedText']
    # print('Translation: %s' % translated) #DEBUG

if __name__ == "__main__":
    trainAI()
    # testAI()
    loadAI()

    listen()


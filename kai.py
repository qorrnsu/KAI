import translator, recognizer, tts, time, vlc
from intent_recognition import IntentClassifier

def play_file():
    p = vlc.MediaPlayer("output.mp3")
    p.play()
    time.sleep(1)
    while p.is_playing():
        time.sleep(1)

def main():
    # classifier = IntentClassifier()
    # classifier.train()
    # classifier.save("k_classifier.pickle")
    classifier = IntentClassifier.load("k_classifier.pickle")

    sentence = recognizer.recognize()
    if sentence[0]:
        # answer = dialogflow.ask(sentence[1])
        confidence = classifier.getProbability(sentence[1]) > 0.3
        if confidence:
            answer = classifier.response(sentence[1])
        else:
            answer = "잘 모르겠어요"

        # print(answer[1])
        if(tts.speak(answer)):
            play_file()
    else:
        # print(sentence[1])
        if(tts.speak(sentence[1])):
            play_file()

    # translated = translator.translate(sentence)['message']['result']['translatedText']
    # print('Translation: %s' % translated) #DEBUG

if __name__ == "__main__":
    main()

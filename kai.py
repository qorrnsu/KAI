import translator, recognizer, dialogflow, tts, time, vlc

def play_file():
    p = vlc.MediaPlayer("output.mp3")
    p.play()
    time.sleep(1)
    while p.is_playing():
        time.sleep(1)

def main():
    sentence = recognizer.recognize()
    if sentence[0]:
        answer = dialogflow.ask(sentence[1])
        # print(answer[1])
        if(tts.speak(answer[1])):
            play_file()
    else:
        # print(sentence[1])
        if(tts.speak(sentence[1])):
            play_file()

    # translated = translator.translate(sentence)['message']['result']['translatedText']
    # print('Translation: %s' % translated) #DEBUG

if __name__ == "__main__":
    main()
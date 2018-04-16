import translator, recognizer, dialogflow


def main():
    sentence = recognizer.recognize()
    if sentence[0]:
        answer = dialogflow.ask(sentence[1])
        print(answer[1])
    else:
        print(sentence[1])


    # translated = translator.translate(sentence)['message']['result']['translatedText']
    # print('Translation: %s' % translated) #DEBUG

if __name__ == "__main__":
    main()
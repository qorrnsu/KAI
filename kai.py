import translator, recognizer

def main():
    sentence = recognizer.recognize()
    print('You said %s' % sentence) #DEBUG
    # translated = translator.translate(sentence)['message']['result']['translatedText']
    # print('Translation: %s' % translated) #DEBUG

if __name__ == "__main__":
    main()
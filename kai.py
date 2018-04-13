import speech_recognition as sr
 
def recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("무엇을 도와 드릴까요?")
        audio = r.listen(source)

    try: 
        print(r.recognize_google(audio, language="ko-KR"))
    except sr.RequestError:
        print("인터넷을 다시 연결해 주세요")

def search():
    pass

def tts():
    pass

def main():
    recognize()
    search()
    tts()

if __name__ == "__main__":
    main()
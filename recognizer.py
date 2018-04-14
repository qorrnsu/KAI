import speech_recognition as sr

def recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("무엇을 도와 드릴까요?")
        audio = r.listen(source)

    try: 
        return r.recognize_google(audio, language="ko-KR")
    except sr.RequestError:
        return "인터넷을 다시 연결해 주세요"
    except:
        return "죄송합니다, 무슨 말씀인지 모르겠어요"
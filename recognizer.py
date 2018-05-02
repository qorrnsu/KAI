import speech_recognition as sr

def recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try: 
        sentence = r.recognize_google(audio, language="ko-KR")
        print('You said: %s' % sentence)
        return (True, sentence)
    except sr.RequestError:
        return (False, "인터넷을 다시 연결해 주세요")
    except:
        return (False, "죄송합니다, 무슨 말씀인지 모르겠어요")

import speech_recognition as sr

def recognize():
    r = sr.Recognizer()
    try: 
        with sr.Microphone() as source:
            # Set wait time until first speech is 3secs, max time foor speech is 5secs
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
        sentence = r.recognize_google(audio, language="ko-KR")
        print('You said: %s' % sentence)
        return (True, sentence)
    except sr.RequestError:
        return (False, "인터넷을 다시 연결해 주세요")
    except sr.WaitTimeoutError:
        return (False, "왜요?")
    except:
        return (False, "죄송합니다, 무슨 말씀인지 모르겠어요")

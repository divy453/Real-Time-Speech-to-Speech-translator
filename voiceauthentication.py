import speech_recognition as sr 
PASS_PHRASE="my voice is my password"

recognizer =sr.Recognizer()
with sr.Microphone()as source:
    print("say your authentication phrase...")
    audio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(audio).lower()
        print("you said:{text}")
        if text==PASS_PHRASE:
             print("access granted")
        else:
            print("access denied")
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Speech recognition error,{e}")

import speech_recognition as sr

r = sr.Recognizer()

def record_text():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.3)
                audio = r.listen(source)
                text = r.recognize_google(audio, language='pt-br')
                return text
        except:
            continue

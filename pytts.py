import pyttsx3

def tts(text):
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)
    engine.say(text)     #出力したい言葉
    engine.runAndWait()

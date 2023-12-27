import pyttsx3

# 1 - Windows [Pro: Fast, Oflline | Con: Less voices, cross-talk] 
def speak(text):
    engine = pyttsx3.init()
    list_voices = engine.getProperty('voices')
    engine.setProperty('voice',list_voices[1].id)   # 0: Male, 1: Female
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    print_text = f"\nNemo : {text}"
    print(print_text)
    engine.say(text)
    engine.runAndWait()
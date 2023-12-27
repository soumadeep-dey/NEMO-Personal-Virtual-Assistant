'''
Explanation:
pause_threshold: is the number of seconds the system will take to recognize the voice after the user has completed their sentence.
timeout: is the maximum number of seconds the system will wait for the user to say something before it throws an OSError exception.
phrase_time_limit: indicates the number of seconds the user can speak. In this case, it is 5. This means that if the user will speak for more than 5 seconds, that speech will not be recognized.
'''
import speech_recognition as sr
from googletrans import Translator

# 1 - Listen: Hindi or English
def listen(time=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print_text = f"Listening..."
        print(print_text)
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source, timeout=0, phrase_time_limit=time)
    try:
        print_text = f"Recognizing..."
        print(print_text)
        #hi: hindi, bn: bengali, en-in: indian
        query = r.recognize_google(audio,language="en", pfilter=1)
        # query = r.recognize_google(audio,language="hi", pfilter=1)
        # query = r.recognize_google(audio, language="bn", pfilter=1)
    except:
        return ""

    query = str(query).lower()
    return query

# 2 - Translation
def translation(text):
    line = str(text)
    t = Translator()
    result = t.translate(line)
    data = result.text      #only extracting the text
    
    print_text = f"\nYou : {data}"
    print(print_text)
    return data

# 3 - Connect
def understand(time=5):
    query = listen(time)
    data = translation(query)
    return data
    

# understand()
from Features.Face.Ear import understand
from Features.Face.Mouth import speak

def isCorrect(topic):
    while True:
        # print(f"{topic}")
        speak("Is information correct?")
        response = understand()
        if "no" in response or "not" in response or "not correct" in response or "wrong" in response:
            return False
        elif "yes" in response or "correct" in response or "perfect" in response:
            return True
        else:
            speak("Sorry, I couldn't understand. Please say that again.")

def isBlank(topic, topic_msg):
    while len(topic) == 0:
        speak(f"You haven't said anything. Please tell {topic_msg.lower()}.")
        # speak(topic_msg)
        topic = understand()
        if len(topic) != 0:
            break
    return topic

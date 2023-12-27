print(">> Starting Jarvis : Wait for a few seconds.")
from Features.Face.Mouth import speak
from Features.Face.Ear import listen, understand
from Features.Verification import *
from Brain.AI_Brain import ReplyBrain
from Features.GreetMe import greet
from getpass import getuser
from Features.DataCheck import isBlank, isCorrect


#Tasks List
def MainExecution():
    
    while True:       
        command = understand()

        if len(command)<=4:
            speak("Sorry, I couldn't understand. Please say that again.")

        elif "go to sleep" in command or "sleep" in command:
            speak("Ok sir , You can call me anytime.")
            break 

        elif "shutdown" in command or "finally sleep" in command:
            speak("Goodbye.\n\t See you soon.")
            exit()
        
        elif "introduce " in command or "intro" in command or "introduction" in command:
            with open("Data//intro.txt", "r") as f:
                intro = f.read()
            speak(intro)
        
        elif "things you can do" in command or "your skills" in command or "skill" in command:
            speak("My skills are:")
            with open("Data//skills.txt", "r") as f:
                skills = f.read()
            print(skills)

        elif "why should we hire you" in command:
            speak("I have excellent communication skills, since you'll need someone to communicate regularly with your customers and other team members as well.")

        elif "set new password" in command:
            if verify_user(isnewpass=1):
                set_pass()

        elif "add new user" in command:
            if verify_user(isnewpass=0,setnewuser=True):
                set_user()
                
        elif "temperature" in command or "weather" in command:
            from Features.Temperature import check_temperature
            speak(check_temperature(command))

        elif "time" in command or "date" in command or "day" in command or "week" in command or "year" in command:
            from Features.DateTime import check_datetime
            speak(check_datetime(command))


        elif "search" in command or "visit" in command or "open" in command or "launch" in command or "start" in command:
            from Features.AppControl import OpenExecute
            OpenExecute(command)

        elif "close" in command:
            from Features.AppControl import CloseExecute
            CloseExecute(command)

        elif "screenshot" in command:
            from Features.Screenshot import take_screenshoot
            take_screenshoot()

        elif "whatsapp" in command or "send message" in command:
            from Features.Whatsapp import send_msg
            send_msg()

        elif "add email" in command or "add new email" in command:
            speak("To set new email please verify yourself.")
            from Features.Email import add_email_to_contact
            if verify_user():
                add_email_to_contact()
        
        elif "set email" in command or "set new email" in command or "reset email" in command:
            speak("To set new email please verify yourself.")
            from Features.Email import set_email_sender
            if verify_user():
                set_email_sender()

        elif "email" in command or "send email" in command:
            speak("To send email please verify yourself.")
            from Features.Email import send_email
            if verify_user():
                send_email()

        elif "make schedule" in command or "add schedule" in command or "set schedule" in command or "add to schedule" in command or "make to do list" in command or "add to do" in command:
            from Features.Schedule import set_schedule
            set_schedule()
        
        elif "show schedule" in command or "my schedule" in command or "schedule" in command or "to do" in command or "new to do" in command or "make to do" in command:
            from Features.Schedule import get_schedule
            get_schedule()

        elif "my location" in command or "location" in command or "current location" in command:
            from Features.GmapLocation import Getmylocation
            Getmylocation()
        
        elif "direction" in command or "show direction" in command or "show me direction" in command:
            from Features.GmapLocation import Getgmaplocation
            subject = ""
            speak("Please tell me your destination location.")
            subject = understand()
            #Blank feild
            subject = isBlank(subject, topic_msg="me your destination location.")

            if isCorrect(subject):
                subject = subject.capitalize()
            else:
                speak("Type the destination location below.")
                subject = input("Enter the destination location: ")
            Getgmaplocation(subject)

        elif 'play' in command:
            import pywhatkit
            song = command.replace('play','')
            speak(f'playing {song}')
            pywhatkit.playonyt(song) 
            
        elif 'marry' in command or 'will you marry me' in command:
            response = "I'm already married to my job.\nWhich is helping you..🤭"
            print("\nAI:",response)
            speak(response)

        elif 'love me' in command or 'i love u' in command:
            response = "I can't feel romantic love but I think you are wonderful.😍"
            print("\nAI:",response)
            speak(response)

        elif 'do i look fat' in command:
            response = "I like the way you are.🤭"
            speak(response)

        elif 'zero divided by zero' in command:
            response = "Imagine that you have zero cookies and you split them evenly among zero friends, how many cookies does each person get? \nSee, it doesn't make sense and cookie monster is sad that there are no cookies, and your friends are sad because they don't exist. \nOh wow, this escalated quickly"
            print("\nAI:",response)
            speak(response)

        elif 'chicken cross the road' in command:
            response = "The Assistant seems to take a pragmatic view of chickens. And sometimes she’s not at all interested in chicken motives."
            print("\nAI:",response)
            speak(response)
            
        elif 'joke' in command or 'jokes' in command:
            import pyjokes
            joke = pyjokes.get_joke()
            speak(joke)
            
        else:
            try:
                reply = ReplyBrain(command)
                speak(reply)
            except:
                speak("Sorry, I currently, don't have this feature.\n\tWill surely add this to my skills in future.\n\tThank you for you suggestion.")

def wakeup_detected():
    print("Say \"wake up\" to start or \"shutdown\" to quit.")
    command = listen()

    if "wake up" in command:
        speak(f"{greet()} I'm Nemo, your virtual assistant. I'm ready to assist you.")
        MainExecution()
    elif "shutdown" in command or "finally sleep" in command:
        speak("Goodbye.\n\t See you soon.")
        exit()

#Main Function
def ThisMain():
    if verify_user():
        speak(f"Welcome, {getuser().capitalize()}!")
        # speak(f"Welcome, Code Heads!")
        speak("Say \"wake up\" to start or \"shutdown\" to quit.")
        while True:
            wakeup_detected()
    else:
        exit()



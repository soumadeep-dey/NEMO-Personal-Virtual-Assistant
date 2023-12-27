from Features.Face.Mouth import speak
from Features.Face.Ear import understand
from Features.DataCheck import isBlank, isCorrect
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from playsound import playsound
import datetime as dt
from plyer import notification
from pygame import mixer

def set_schedule():
    tasks = []
    speak("Do you want to clear all previous tasks?")
    response = understand()
    response = isBlank(response, "Do you want to clear all previous tasks?")
    tasks_len = 0
    if "yes" in response or "clear" in response or "delete" in response or "erase" in response:
        with open("Data//schedule.txt","w") as f:
            f.write("")
    elif "no" in response or "keep" in response or "leave it" in response or "dont" in response:
        with open("Data//schedule.txt","r") as f:
            tasks_len = len(f.readlines())

    speak("Type below how many tasks do you want to add in your schedule?")
    tasks_no = int(input("Enter no of tasks: "))
    speak("Type the tasks you want to add in your schedule below")
    for i in range(tasks_no):
        tasks.append(input("Enter the task: "))
        with open("Data//schedule.txt",'a') as f:
            f.write(f"{tasks_len+i+1}. {tasks[i]}\n")

def get_schedule():
    with open("Data//schedule.txt","r") as f:
            tasks_len = len(f.readlines())
    if tasks_len == 0:
        speak("Your schedule is empty.")
        return
    else:
        with open("Data//schedule.txt","r") as f:
            tasks = f.read()
        #Music
        mixer.init()
        mixer.music.load("Data//notification.mp3")
        mixer.music.play()

        #notification
        notification.notify(
            title = "My Schedule:",
            message = tasks,
            timeout = 10
        )

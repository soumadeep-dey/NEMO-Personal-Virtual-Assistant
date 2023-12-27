import pyautogui
import os
from Features.Face.Mouth import speak

def take_screenshoot():
    speak("Taking screenshot")
    img = pyautogui.screenshot()
    img.save(r"C:\Users\SOUMADEEP\Pictures\Screenshots\ss.jpg")
    speak("Screenshot taken.")
    os.startfile(r"C:\Users\SOUMADEEP\Pictures\Screenshots\ss.jpg")
    speak("Showing screenshot")

# take_screenshoot()
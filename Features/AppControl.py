import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from getpass import getuser
from Features.Face.Mouth import speak


user_name = getuser()
# App list:
known_apps = {
    "chrome": r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    "microsoft edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "vlc media player": r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe",
    "notepad": r"C:\Windows\system32\notepad.exe",
    "command prompt": r"C:\Windows\system32\cmd.exe",
    "brave browser": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    "vs code": r"C:\Users\SOUMADEEP\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "telegram": r"C:\Users\SOUMADEEP\AppData\Roaming\Telegram Desktop\Telegram.exe",
    "file explorer": r"C:\Windows\explorer.exe"
}


def OpenExecute(app_name):

    app_name = str(app_name).lower()

    # Website:
    if "search" in app_name or "visit" in app_name or ".com" in app_name or ".org" in app_name or ".co.in" in app_name:
        if "visit" in app_name:
            site_name = app_name.replace("visit ", "")
        if "open" in app_name:
            site_name = app_name.replace("open ", "")
        elif "launch" in app_name:
            site_name = app_name.replace("launch ", "")
        elif "start" in app_name:
            site_name = app_name.replace("start ", "")
        elif "search" in app_name:
            site_name = app_name.replace("search ", "")

        speak(f"Openning {site_name}")
        if ".com" in site_name or ".org" in site_name or ".co.in" in site_name:
            link = f"http://www.{site_name}"
            webbrowser.open(link)
            return speak(f"{site_name} successfully opened.")

        else:
            link = f"https://www.google.com/search?q={site_name}"
            webbrowser.open(link)
            return speak(f"{site_name} successfully opened.")

    # Application:
    elif "open" in app_name or "launch" in app_name or "start" in app_name:
        if "open" in app_name:
            app_name = app_name.replace("open ", "")
        elif "launch" in app_name:
            app_name = app_name.replace("launch ", "")
        elif "start" in app_name:
            app_name = app_name.replace("start ", "")

        try:
            present = False
            if app_name in known_apps:
                present = True
                os.startfile(known_apps[app_name])
                speak(f"Openning {app_name}")
                sleep(0.6)
                return speak(f"{app_name} successfully opened.")

            assert present == True

        except:
            speak(f"Openning {app_name}")
            pyautogui.press('super')
            sleep(0.5)
            keyboard.write(app_name)
            sleep(1)
            keyboard.press("enter")
            sleep(1)
            return speak(f"{app_name} successfully opened.")

    return speak("Sorry, I've never heard about it.")

close_apps = {
    "chrome": "chrome",
    "word": "WINWORD",
    "excel": "EXCEL",
    "powerpoint": "POWERPNT",
    "microsoft edge": "msedge",
    "browser": "msedge",
    "vlc media player": "vlc",
    "notepad": "notepad",
    "command prompt": "cmd",
    "brave browser": "brave",
    "brave": "brave",
    "vs code": "Code",
    "telegram": "Telegram",
    "paint": "mspaint",
}

def CloseExecute(app_name):
    app_name = str(app_name).lower()
    app_name = app_name.replace("close ", "")

    speak(f"Closing {app_name}.")

    # Website
    if "one tab" in app_name or "1 tab" in app_name:
        pyautogui.hotkey("ctrl", "w")
        return speak(f"{app_name} closed successfully.")

    elif "two tab" in app_name or "2 tab" in app_name:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        return speak(f"{app_name} closed successfully.")

    elif "three tab" in app_name or "3 tab" in app_name:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        return speak(f"{app_name} closed successfully.")

    elif "all tab" in app_name:
        pyautogui.hotkey("ctrl", "shift", "w")
        sleep(0.5)
        return speak(f"{app_name} closed successfully.")

    # Application
    try:
        if app_name in close_apps:
            status = os.system(f"taskkill /f /im {close_apps[app_name]}.exe")
        else:
            status = os.system(f"taskkill /f /im {app_name}.exe")
        assert status == 0
        speak(f"{app_name} closed successfully.")

    except:
        speak("Currently the application is not opened.")

# OpenExecute('open vs code')
# CloseExecute('close vs code')

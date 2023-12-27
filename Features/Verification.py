import Features.Database as db
from getpass import getpass, getuser
from Features.Face.Mouth import speak


def set_pass():
    speak("Enter your new password below:")
    new_pass = getpass("Enter new pass: ")
    db.Updatepassword(getuser(), new_pass)
    speak("New password has been changed successfully.")
    
def set_user():
    print("--- If you don't know your user name type \"whoami\" in command prompt.--- ")
    speak("Enter new user name below")
    new_user = input("Enter user name: ")
    #Password is default(1234) but can be changed with password parameter
    db.Addnewuser(new_user)
    speak("New user added successfully.")
   
def verify_user(isnewpass=0,setnewuser=False):
    info=db.Infodetails(getuser())
    known_users = info[0]
    u_pwd = info[1]
    isadmin=info[2]

    if getuser() != known_users:
        speak("User Authentication Failed!\nPlease login through a verified account or contact your admin to get verified.")
        return False
    else:
        if setnewuser == True and isadmin != True:
            return False
        speak("User Authentication Successful!")
        for i in range(3):
            if isnewpass == 0:
                speak("Please type your password below:")
            else:
                speak("Enter your current password below:")
            p_pwd = getpass(prompt='Enter password: ')
            # with open("user_pwd.txt","r") as f:
            #     u_pwd = f.read()
            #Pass Check
            if p_pwd == u_pwd:
                return True
            #Max attempt check
            elif i==2 and p_pwd != u_pwd:
                speak("Maximum attempts exceeded.\nPlease contact admin and try again later.")
                return False
            else:
                speak(f"Wrong password!\n[Attempts Left: {3-(i+1)}]\nTry again.")


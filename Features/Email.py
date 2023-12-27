# Create app password for email: https://myaccount.google.com/u/4/apppasswords

import os
from email.message import EmailMessage
import ssl, smtplib
from Features.Face.Ear import understand
from Features.Face.Mouth import speak
from Features.DataCheck import isBlank, isCorrect
import Features.Database as db

def add_email_to_contact():
        speak("Please type the name of the person below")
        speak("Please type new email id below")
        email_receiver = input("Enter new email id: ")

        #Blank feild
        email_receiver = isBlank(email_receiver, topic_msg="new email id to add.")

        #Same email
        emailinfo=db.Emaildetails()
        if email_receiver == emailinfo[0]:
            speak("You have entered the same current EmailID")
            return
        newname=input("Enter the name: ")
        db.Add_email(newname, email_receiver)
        speak(f"{newname} has been successfully added in your contact")

def set_email_sender():
    #Email ID change
    speak("Please type new email id below")
    new_email = input("Enter new email id: ")
    emailinfo=db.Emaildetails()
    if new_email == emailinfo[0]:
        speak("You have entered the same current EmailID")
        return

    print("--- If you don't know your app password visit \"https://myaccount.google.com/u/4/apppasswords\" to generate new password. --- ")
    speak("Please type your app password for the provided email id below")
    new_pass = input("Enter app password: ")

    db.SetEmailID(new_email,new_pass)
    speak("Your Email and Password for provided email id has been changed successfully.")

def ifyes(contact):
     while True:
        speak(f"Do you want to save this email {contact} in your contact?")
        response = understand()
        if "no" in response or "not" in response or "not correct" in response or "wrong" in response:
            return False
        elif "yes" in response or "correct" in response or "perfect" in response:
            return True
        else:
            speak("Sorry, I couldn't understand. Please say that again.")

def send_email():
    #Fetch from contacts
    knowninfo=db.Known_email()
    knownemails=knowninfo[0]

    #Fetch admin id, pass
    emailinfo=db.Emaildetails()
    email_sender=emailinfo[0]
    email_pass=emailinfo[1]

    #Display contacts:
    print("Your Contact List:")
    print(knownemails)
    
    #Receiver email id
    speak("Whom to send mail?")
    email_receiver = understand()
    #Blank feild
    email_receiver = isBlank(email_receiver, topic_msg="Whom to send mail?")

    if email_receiver in knownemails:
        id=db.Known_email(email_receiver)
        if id[2] == "":
            speak("There seems to be a problem to find emailid, Please contact admin")
            return
        else:
            email_receiver = id[2]
    else:
        speak("The receiver is not in your contacts. Please type the email id below.")
        email_receiver = input("Enter receiver\'s email id: ")
    
    #Subject
    subject = ""
    speak("What's the subject?")
    subject = understand()
    #Blank feild
    subject = isBlank(subject, topic_msg="What's the subject?")
    
    if isCorrect(subject):
        subject = subject.capitalize()
    else:
        speak("Type the subject of the email below.")
        subject = input("Enter subject of the email: ")

    #Body
    body = """"""
    speak("What's the email body?")
    body = understand(time=10)
    #Blank feild
    body = isBlank(body, topic_msg="What's the email body?")
    
    if isCorrect(body):
        body = body.capitalize()
    else:
        speak("Type the email body below.")
        body = input("Enter email body: ")
    
    #Email
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = str(subject)
    em.set_content(str(body))

    context = ssl.create_default_context()
    try:
        #server, port, context
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_pass)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        speak(f"Email has been sent to {email_receiver} successfully.")

        id=db.Known_email(email_receiver)
        if email_receiver not in id[1]:
            try:
                if ifyes(email_receiver):
                    speak("Please type the name of the person below")
                    newname=input("Enter the name: ")
                    db.Add_email_receiver(newname, email_receiver)
                    speak(f"{newname} has been successfully added in your contact")
                    
            except:
                speak(f"Failed to add the email to your contact.")
            
    except:
        speak(f"Failed to sent email to {email_receiver}.")

# send_email()
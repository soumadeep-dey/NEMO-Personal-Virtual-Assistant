# NEMO (Voice Controlled Personal Virtual Assistant)

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Frontend](https://img.shields.io/badge/Frontend-Tkinter-fcba03) ![Backend](https://img.shields.io/badge/Backend-MongoDB-darkgreen) ![Libraries](https://img.shields.io/badge/Libraries-SpeechRecognition_|_GoogleTranslate_|_OpenAI_|_BeautifulSoup_|_PyAutoGUI_|_GeoPy_|_PyWhatKit_|_PyGame_|_PyAudio-red)

#### 🔗 [Live Project Demonstration Video Link](https://youtu.be/s6moWG6B47I?si=7vL11BywWyH08WSu)

![Nemo text logo](https://github.com/soumadeep-dey/NEMO-Personal-Virtual-Assistant/assets/111021618/cbdc154c-ad57-4103-8a77-be89344a8cb0)

**NEMO** stands for **Naturally Evolving Model.**

NEMO is a voice controlled personal virtual assistant technology driven by artificial intelligence and machine learning that adeptly responds to voice commands, executes diverse tasks, and engages with users in a human-like manner.

## Scope of the project:

* Voice Controlled Optimized Human-like Query Resolver using Artificial Intelligence
* Voice Controlled Application Control
* Voice Controlled E-messaging: email, whatsapp
* Voice Controlled Media Control
* Voice Controlled Web/Website Searching
* Voice Controlled Direction and Navigation
* Narrated Notes, Task/Appointment Scheduling
* Utility management: time, date, weather forecast
* Contact/Email Management

## Voice Controlled Features:

1. Optimized Human-like Query Resolver using Artificial Intelligence
2. Interact and Chat in a Human-like mannner
3. Listen to Jokes
4. Get Date and Time Update
5. Get Weather Forecast Update
6. Google Search Support
7. Search and Play anything on Youtube
8. Play any Song
9. Control your browser
10. Open and Close any App or Application
11. Visit any Website (e.g wikepedia, gmail, ) that has .in/.com/.org
12. Open any Social Media sites (e.g facebook, twitter, instagram)
13. Send Emails
14. Send Whatsapp message
15. Get Current Geo Location
16. Get Direction or Navigation to Places
17. Capture Screenshot
18. Schedule your day
19. Create To-do list
20. Email and Contact management

## How It Works?
![DFD](https://github.com/soumadeep-dey/NEMO-Personal-Virtual-Assistant/assets/111021618/76759d02-a698-4d24-9a4a-a6265b304f15)


## Market 

![Tasks](https://github.com/soumadeep-dey/NEMO-Personal-Virtual-Assistant/assets/111021618/c41e4442-3572-479b-b1e4-45f9af094508)

## Business Model

![Bussiness](https://github.com/soumadeep-dey/NEMO-Personal-Virtual-Assistant/assets/111021618/e0ca1f0c-456c-46f4-bd26-4644a5b18ac5)

## How to run the project locally?

1. Clone or download this repository to your local machine.
2. `cd` into the cloned folder.
3. Install virtual environment python package using command:

   ```
   pip install virtualenv
   ```
4. Create a virtual environment using command:

   ```
   python3 -m venv [Enter Folder name]
   ```
5. Activate virtual environment using command:

   ```
   source [virtual environment name]/bin/activate
   ```
6. Install all the libraries mentioned in the [requirements.txt](https://github.com/soumadeep-dey/Movie-Recommendation-System/blob/main/requirements.txt) file with the command:

   ```
    pip install -r requirements.txt
   ```
7. Create a `contacts.text` file inside `Data` folder and paste the provided template inside and edit it accordingly:

   ```
   {
        "name1": "+91(whatsapp number)",
        "name2": "+91(whatsapp number)",
        "name3": "+91(whatsapp number)"
    }
   ```
8. Get your API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
9. Create a `Api.text` file inside `Data` folder and paste the API key insde the file as follows:

   ```
   "YOUR_API_KEY"
   ```
10. Downlaod and install MongoDB Compass from [mongodb.com/products/tools/compass](https://www.mongodb.com/products/tools/compass)
11. Save and Connect to URI:  `mongodb://localhost:27017`
12. Create a new database called `NemoVA` and a new collection called `Nemo_DB`
13. Click on `Import data` and from `DataBase Template` folder, select the provided database template: [DemoDB.json](https://github.com/soumadeep-dey/NEMO-Personal-Virtual-Assistant/blob/main/DataBase%20Template/DemoDB.json)
14. Add Admin, User name and password to the template feilds:
    ![MongoDb template](https://github.com/soumadeep-dey/NEMO-Personal-Virtual-Assistant/assets/111021618/58e49290-833d-4d7a-a342-330b2c3cc1da)
15. Create a App Password for sending email from [myaccount.google](https://myaccount.google.com/u/4/apppasswords) and add the Email ID using which the password was created and the password to the template feild provided:

    ```
    {
        "_id": {
            "$oid": "643f901e88aeee01e9a50871"
        },
        "IsAdmin": true,
        "EmailID": "Enter Sender's Email ID from which you want to send",
        "Emailpassword": "Create App Password from https://myaccount.google.com/u/4/apppasswords"
    }
    ```
16. Fill up Receiver's Email ID and Contact name and add more using the provided template:

    ```
    {
        "_id": {
            "$oid": "64410cac9e93a40e3eb7b3ff"
        },
        "Emailname": "Enter short contact name for easy & quick reference",
        "EmailID": "Enter email ID"
    }

    ```
17. Run the python file: [Nemo_GUI (Run This).py ](https://github.com/soumadeep-dey/NEMO-Personal-Virtual-Assistant/blob/main/Nemo_GUI%20(Run%20This).py)
18. Click on the Nemo icon and enjoy your Personal Assitant - **NEMO**

Hurray! That's it. 🥳

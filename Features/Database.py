import pymongo
 
#Connecting to localhost client
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Database Name
db = client["NemoVA"]
# Collection Name
col = db["Nemo_DB"]


def Infodetails(uname):
    name = ""
    password = ""
    isadmin=False
    isuser=False
    info=col.find({},{ "_id": 0})
    for items in info:
        for i in items.items():
            if i[0] == "Adminname" and uname == i[1]:
                name=i[1]
                isadmin=True
            if i[0] == "Adminpassword" and isadmin == True:
                password=i[1]
            elif i[0] == "Username" and uname == i[1]:
                name=i[1]
                isuser=True
            elif i[0] == "Userpassword" and isuser == True:
                password=i[1]
        if isuser == True or isadmin == True:
            break
    return name,password,isadmin

def Updatepassword(name,password):
    q = { "Adminname": name }
    newpass = { "$set": { "Adminpassword": password } }
    col.update_one(q, newpass)

def Addnewuser(uname,upassword="1234"):
    newuser = { "Username": uname, "Userpassword": upassword }
    col.insert_one(newuser)

def Emaildetails():
    info=col.find({"IsAdmin": True},{ "_id": 0,"EmailID":1,"Emailpassword":1})
    for items in info:
        if items.__len__() <= 0:
            continue
        for i in items.items():
            if i[0]=="EmailID":
                emailid=i[1]
            if i[0]=="Emailpassword":
                emailpassword=i[1]
    return emailid,emailpassword

def SetEmailID(EmailID,Password):
    emailinfo=Emaildetails()
    oldemailid=emailinfo[0]
    q = { "EmailID": oldemailid }
    newpass = { "$set": { "EmailID": EmailID, "Emailpassword": Password } }
    col.update_one(q, newpass)

def Add_email_receiver(ename,emailID):
    newcontact = { "Emailname": ename, "EmailID": emailID }
    col.insert_one(newcontact)

def Known_email(srch=""):
    ename=""
    eid=""
    id=""
    tempid=""
    tempname=""
    count=0
    info=col.find({},{ "_id": 0,"Emailname":1,"EmailID":1})
    for items in info:
        if items.__len__() <= 0:
            continue
        for i in items.items():
            if i[0]=="Emailname":
                tempname=i[1]
                ename += i[1] + ",\n"
            if i[0]=="EmailID":
                tempid=i[1]
                eid +=i[1] + ",\n"
        if srch !="":
            if srch == tempname:
                id=tempid
    return ename.rstrip(',\n'),eid.rstrip(',\n'),id


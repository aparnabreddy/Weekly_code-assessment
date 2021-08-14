import pymongo,smtplib
import re
import logging
from datetime import datetime 

client=pymongo.MongoClient("mongodb://localhost:27017/") #Establishing Connection
mydatabase=client['BloodbankDb'] #Database
collection_name=mydatabase['donors']  #Collection


donorlist=[]
fetch=[]  

class BloodBank:
    def adddonordetails(self,name,address,blood_group,pincode,mob_no,email,last_donated_date,place):
        dict={"name":name,"address":address,"bloodgroup":blood_group,"pincode":pincode,"mobileno":mob_no,"last_donated_date":last_donated_date,"place":place}
        return dict
obj=BloodBank()

def validation_of_donors(name,mob_no,address,blood_group,email):
    valname=re.search("[A-Za-z]{0,25}$",name)
    valmob_no=re.search("^[7-9]{1}[0-9]{9}$",mob_no)
    valaddress=re.search("^[A-Z]{1}[A-Za-z]{0,50}$",address)
    valemail= re.match(r"[\w-]{1,20}@\w{2,20}\.\w{2,3}$",email)
    valblood_group=re.search("^[A-Z]{1,2}[+]|[-]$",blood_group)
    if  valname and valmob_no and valaddress and valemail and valblood_group:
        return True
    else:
        return False 

while(True):
    print("\n Bloodbank Bank Management System")
    print("\n 1. Add donor:")
    print("\n 2. search donors based on blood group:")
    print("\n 3. Search donors based on blood group and place:")
    print("\n 4. Update all donor details with their mobile number:")
    print("\n 5. Delete the donor using mobile number:")
    print("\n 6. Display total number of donors on each blood group:")
    print("\n 7.Immediate notification to all via mail")
    print("\n 8. Exit")

    try:
        choice=int(input("Enter your choice : "))
    except:
        logging.error("Choice should be integer")

    if choice==1:
        name=input("Enter the donor name : ") 
        address=input("Enter the donor address: ")
        pincode=input("Enter the pincode: ")
        blood_group=input("Enter the blood group: ")
        mob_no=int(input("Enter donor's mobile number: "))
        email=input("Enter the donor's mail id : ") 
        last_donated_date=input("Enter the date: ")
        place=input("Enter the place: ")
        data=obj.adddonordetails(name,address,pincode,blood_group,mob_no,email,last_donated_date,place) 
        donorlist.append(data)
        result=collection_name.insert_many(donorlist)
        print(result.inserted_ids)
        if validation_of_donors(name,mob_no,address,blood_group,email)==True:
            data=obj.adddonordetails(name,address,pincode,blood_group,mob_no,email,last_donated_date,place) 
            donorlist.append(data)
            result=collection_name.insert_many(donorlist)
            print(result.inserted_ids)
                
        else:
            logging.error("VALIDATION ERROR!!!")
            break

     
    if choice==2:
        bgroup=input("\n Enter blood group to search:")
        result= collection_name.find({"blood_group":bgroup},{"_blood_group":0}) 
        for j in result:
            print(j)
        donorlist.clear() 

    if choice==3:
        bgroup=input("\n Enter blood group to search:")
        dplace=input("\n Enter place to search:")
        result=collection_name.find({"$and":[{"blood_group":bgroup},{"place":dplace}]})
        for i in result:
            fetch.append(i)
        print(fetch) 


    if choice==4:
        number=int(input("\n Enter the donor's mobile number, whose  details are to be updated:"))
        newaddress=input("\n Enter address to be updated:")
        newplace=input("\n Enter the place to be updated:")
        result=collection_name.update_one({"mobileno":number},{"$set":{"address":newaddress,"place":newplace}})
        print(fetch)  


    if choice==5:
        del_donor=int(input("\n Enter the donor's mobile number whose details to be deleted:"))
        result=collection_name.delete_many({"mobileno":del_donor})
        print(fetch) 


    if choice==6:
        result=collection_name.aggregate([{"$group": {"_id":"$blood_group","no_of_donors":{"$sum":1}}}])
        for j in result:
            print(j)


    if choice==7:
        bldgrp=input("Enter the required blood group: ")
        Hospital=input("Enter the name of the hospital where blood required: ")
        message="Immediately want"+bldgrp+ "blood group in "+Hospital+ "hospital"
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login("sowmya070721@gmail.com","sowmya@0707")
        connection.sendmail("sowmya070721@gmail.com",email,message)
        connection.quit
        print("Mail sent")

        logging.info("Immediate mail sent")
                

    if choice==8:
        break
import re,logging,json,smtplib
student_list=[]
class Student:
    def studentDetails():
        name=""
        rollnum=0
        adminum=0
        college=""
        parentname=""
        mobno=0
        emailid=""
class marks:
    def stumarks():
            sub1mark=0
            sub2mark=0
            sub3mark=0
            sub4mark=0
            sub5mark=0

class sem1Result(Student,marks):
    def addstudentdetails(self,name,rollnum,adminum,college,parentname,mobno,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        # sub1mark=0
        # sub2mark=0
        # sub3mark=0
        # sub4mark=0
        # sub5mark=0
        total=sub1mark+sub2mark+sub3mark+sub4mark+sub5mark
        dict1={"name":name,"rollnum":rollnum,"adminum":adminum,"college":college,"parentname":parentname,"mobno":mobno,"emailid":emailid,"sub1mark":sub1mark,"sub2mark":sub2mark,"sub3mark":sub3mark,"sub4mark":sub4mark,"sub5mark":sub5mark,"total":total}
        student_list.append(dict1)
obj1=sem1Result()

def validation(name,rollnum,adminum,mobno,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
    valname=re.match("^[A-Z]{1}[a-z{2,30}]$",name)
    valroll=re.match("[0-9]{0,7}$",rollnum)
    valadmin=re.match("[0-9]{0,7}$",adminum)
    valmob=re.match("^[6-9]\d{9}",mobno)
    valemail=re.match("[a-z0-9]{5,25}@[a-z]+\.[a-z]{2,5}$",emailid)
    valsub1=re.match("^(50 | [0-4][0-9]?)$",sub1mark)
    valsub2=re.match("^(50 | [0-4][0-9]?)$",sub2mark)
    valsub3=re.match("^(50 | [0-4][0-9]?)$",sub3mark)
    valsub4=re.match("^(50 | [0-4][0-9]?)$",sub4mark)
    valsub5=re.match("^(50 | [0-4][0-9]?)$",sub5mark)
    if valname and valroll and valmob and valemail and valsub1 and valsub2 and valsub3 and valsub4 and valsub5:
        return True
    else:
        return False


while(True):
    print("1.Add Student details with marks")
    print("2.Display student API in json file")
    print("3.Display students API based on ranking ")
    print("4.send mail to parents")
    print("5.Exit")
    try:
        choice=int(input("Enter your choice: "))
    except:
        logging.error("Choice should be an integer")
    if choice==1:
        while(True):
            
            name=input("Enter student name: ")
            rollnum=int(input("Enter student rollnum: "))
            adminum=int(input("Enter student adminum: "))
            college=input("Enter college name: ")
            parentname=input("Enter student's parentname: ")
            mobno=int(input("Enter mobile no: "))
            emailid=input("Enter emailid: ")
            sub1mark=int(input("Enter sub1 marks: "))
            sub2mark=int(input("Enter sub2 marks: "))
            sub3mark=int(input("Enter sub3 marks: "))
            sub4mark=int(input("Enter sub4 marks: "))
            sub5mark=int(input("Enter sub5 marks: "))
            if validation(name,rollnum,adminum,mobno,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):

                obj1.addstudentdetails(name,rollnum,adminum,college,parentname,mobno,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)
            else:
                logging.error("Please enter correct details and try again")
                continue
            break
    if choice==2:
        json_object=json.dumps(student_list)
        with open("student.json",'w+') as output:
            output.write(json_object)
    if choice==3:
        ranking=sorted(student_list,key=lambda i:i['total'],reverse=True)
        json_object=json.dumps(ranking)
        with open("student_rank.json",'w+') as output:
            output.write(json_object)
    # if choice==4:
    #     msg=""
    #     connection=smtplib.SMTP("smtp.gmail.com",587)
    #     connection.starttls()
    #     connection.login("sowmya070721@gmail.com","sowmya@0707")
    #     connection.sendmail("sowmya070721@gmail.com","aparnabreddy26@gmail.com",msg)
    #     print("email has successfully send")
    #     connection.quit()
    if choice==5:
        break
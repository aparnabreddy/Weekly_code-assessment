Totalamount=0
while(True):
    print("show Menu")
    print("1. Tea                   -Rs.7")
    print("2. Coffee                -Rs.10")
    print("3. Masala Dosa            -Rs.50")
    print("4. View bill and Email")
    choice=int(input("Enter your choise:"))
    if choice==1:
        Totalamount=Totalamount+7
    elif choice==2:
        Totalamount=Totalamount+10
    elif choice==3:
        Totalamount=Totalamount+50
    elif choice==4:
        break
print(Totalamount)

import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("969kiran969@gmail.com","Kiran@969")
message=Totalamount
connection.sendmail("969kiran969@gmail.com","rachapallikirankumar969@gmail.com",message)
print("email sent successfully")
connection.quit()
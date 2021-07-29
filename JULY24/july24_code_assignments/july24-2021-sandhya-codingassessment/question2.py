import smtplib
string1=input("enter the string1")
s=string1.upper()
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("practicedigital12@gmail.com","sandhya9@9")
message=s[0:5]
connection.sendmail("practicedigital12@gmail.com","gulshan062132@gmail.com",message)
connection.quit()
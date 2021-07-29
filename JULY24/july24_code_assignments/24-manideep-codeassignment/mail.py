import smtplib
string=input("enter a string")
s=string.upper()
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("manideepkotha324@gmail.com","mani@9324")
message=s[0:6]
connection.sendmail("manideepkotha@gmail.com","kothamanideep123@gmail.com",message)
connection.quit()
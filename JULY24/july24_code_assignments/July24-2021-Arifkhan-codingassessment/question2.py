import smtplib
name=input("enter the string")
pst=name[0:6]
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
connection.sendmail("Arifkhanstar0786@gmail.com","barfikhan78621@gmail.com",pst)
print("INDIA IS MY COUNTRY")
print(pst)
connection.quit()
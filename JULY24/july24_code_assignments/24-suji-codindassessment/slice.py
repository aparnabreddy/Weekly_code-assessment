import smtplib
x=input("enter the string:")
a=slice(5)
b=print(x[a])
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("sujivennapusa2000@gmail.com","suji1806")
message="INDIA"
connection.sendmail("sujivennapusa2000@gmail.com","vennapusasuji463@gmail.com",x[a])
print("email sent successfully")
connection.quit() 
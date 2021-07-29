import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("969kiran@gmail.com","Kiran@969")
str=input("enter a string:")
x=slice(5)
connection.sendmail("969kiran969@gmail.com","rachapallikirankumar969@gmail.com",x)
print(str[x])
connection.quit()
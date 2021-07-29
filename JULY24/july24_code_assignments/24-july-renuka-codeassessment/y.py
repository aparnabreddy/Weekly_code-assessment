import smtplib,ssl
email="chavala.sridhar476@gmail.com"
password="Sridhar123@"
message=input("enter a message")
message=message[:5]
receiver="chavala.renuka@gmail.com"
port=465
sslcontext=ssl.create_default_context()
connection=smtplib.SMTP_SSL("smtp.gmail.com",port,context=sslcontext)
connection.login(email,password)
connection.sendmail(email,receiver,message)
print("message sent")
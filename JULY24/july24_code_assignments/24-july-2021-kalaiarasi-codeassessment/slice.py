import smtplib
connection =smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("kalai.iprimed@gmail.com","Kalai@2404")
str1=input("enter:")
message=str1[0:5]
connection.sendmail("kalai.iprimed@gmail.com","pkalai2404@gmail.com",message)
print("email send")
connection.quit()
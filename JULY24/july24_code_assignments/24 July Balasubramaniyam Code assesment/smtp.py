import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("balu08062000@gmail.com","balu@123")
String=input("Enter a String: ")
message=String[:5]
print(message)
connection.sendmail("balu08062000@gmail.com","balusaravanan862@gmail.com",message)
connection.quit()
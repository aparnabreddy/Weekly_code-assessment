import smtplib

statement = str(input("enter a statement: "))
msg = (slice(6))
message= (statement[msg])
print(message)
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("chedivya1998@gmail.com","Welcome@2169")
connection.sendmail("chedivya1998@gmail.com","amarthiga@gmail.com",message)
print("the email has sent successfully")
connection.quit()

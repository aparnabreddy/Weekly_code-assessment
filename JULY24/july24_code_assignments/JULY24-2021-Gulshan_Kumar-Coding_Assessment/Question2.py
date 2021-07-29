import smtplib
string = input('enter the string')
s = string.upper()
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("gulshan062132@gmail.com","Gullu@2132")
message=s[0:5]
connection.sendmail("gulshan062132@gmail.com","gulshankumar060699@gmail.com",message)
connection.quit()
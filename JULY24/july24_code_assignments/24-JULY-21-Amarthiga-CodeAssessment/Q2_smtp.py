import smtplib as send 

sentence = (str(input("Which is your country?")))
msg=(slice(6))
x= (sentence[msg])
print(x)

connection=send.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("amarproject2021@gmail.com", "remoteGIS24")
connection.sendmail("amarproject2021@gmail.com","amarthiga@gmail.com",x)
print("Email has sent successfully")
connection.quit()



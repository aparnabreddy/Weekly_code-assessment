import smtplib
li=input("Enter the string")


msg=li[0:6]
#print(msg)


connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("ridhimathur10@gmail.com","ridhima@10")
connection.sendmail("ridhimathur10@gmail.com","hariompateldada@gmail.com",msg)
print("email has successfully send")
connection.quit()
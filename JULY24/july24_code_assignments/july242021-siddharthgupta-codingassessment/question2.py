import smtplib
li=input("Enter the string")


msg=li[0:6]
#print(msg)

  
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("hariompateldada@gmail.com","Sparsh@01")
connection.sendmail("hariompateldada@gmail.com","ridhimathur10@gmail.com",msg)
print("email has successfully send")
connection.quit()
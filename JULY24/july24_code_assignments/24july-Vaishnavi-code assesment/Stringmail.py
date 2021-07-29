import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
message="Hello , I am Vaishnavi"
connection.sendmail("vaishnavi.p6521@gmail.com", "priya.hajela358@gmail.com", message)
data=input("Enter a string:")
x=slice(5)
print(data)
print(data[x])
print("Email sent successfully")
connection.quit()
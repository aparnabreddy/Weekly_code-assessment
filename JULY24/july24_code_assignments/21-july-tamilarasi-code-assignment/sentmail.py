import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587) #connection smtp
connection.starttls()
connection.login("tamilarasiiprimed@gmail.com","Iprimed@123") 
data=input("Enter the string:")
message=data[:5]
connection.sendmail("tamilarasiiprimed@gmail.com","tamilarasiifet@gmail.com",message) 
print("mail send successfully")
connection.quit()
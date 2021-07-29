import smtplib
string="INDIA IS MY COUNTRY"
print(string[0:6])
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("krupamh0@gmail.com","panipuri23@")
message="INDIA"
connection.sendmail("krupa2332@gmail.com","krupa9927@gmail.com",message)
connection.quit()
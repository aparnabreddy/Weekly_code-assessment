import re
import smtplib

x=0
y=0
z=0

while(True):
    #print("\n")
    print("Choose an option from menu")
    print("1. Tea (Rs.7)")
    print("2. Coffee (Rs.10)")
    print("3. Masala Dosa (Rs.50)")
    print("4. View Bill and Email")
    def menu_val(choice):
        cv=re.search("^[1-4]$",choice)
        if cv:
            print("Option is selected",choice)
        else:
            print("Invalid Option")
    choice1=(int(input("Select your option: ")))
    if choice1==1:
        print("Tea is selected")
        def tea(a):
            return 7*a
        x = int(input("Please, Enter number of Tea you want to order: "))
        print(tea(+x)) 
    if choice1==2:
        print("Coffee is selected")
        def coffee(b):
            return 10*b
        y = int(input("Please, Enter number of Coffee you want to order: "))
        print(coffee(+y))
    if choice1==3:
        print("Masala Dosa is selected")
        def masala(c):
            return 50*c
        z = int(input("Please, Enter number of Masala Dosa you want to order: "))
        print(masala(+z))
    if choice1==4:
        print("Billing is processing")
        def bill(i):
            return (7*x)+(10*y)+(50*z)
        n=(7*+x)+(10*y)+(50*z)
        print("Total bill of your order:")
        print(bill(n))
        break
    else:
        print(" ")

# Tea= str(tea(+x))
# Coffee = str(coffee(+y))
# MasalaDosa = str(masala(+z))
Total= str(bill(n))
#message = f"ABC RESTAURANT: Billed item Description 1. Tea rate {Tea} 2. Coffee rate {Coffee} 3. Masala Dosa rate {MasalaDosa} The Grand Total: {Total}"
#message = f"""         
            #   1. Tea rate           {Tea} 
            #   2. Coffee rate        {Coffee} 
            #   3. Masala Dosa rate   {MasalaDosa} 
            #   The Grand Total:      {Total}
            #   Happy purchasing, Visit us again! :)"""
#print(message)
message = f"Grand Total of the Order Rs.{Total}"

try:
    email_id = input("Please, enter your email ID: ")
    val3 = "r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if val3:
        print("valid email id")
    else:
        print("invalid id")
except:
    print("error in validation")

connection = smtplib.SMTP ("smtp.gmail.com",587)
connection.starttls()
connection.login("amarproject2021@gmail.com","Geo@2124")
connection.sendmail("amarproject2021@gmail.com",email_id, message)
print("The bill has sent successfully to the customer Email ID")
print("Please, check the bill.")
print("Happy purchasing, Visit us again! :)")
connection.quit()

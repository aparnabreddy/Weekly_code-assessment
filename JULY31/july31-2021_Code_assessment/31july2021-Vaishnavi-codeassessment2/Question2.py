import re
import smtplib
while(True):
    name=input("Please Enter Customer Name :")
    email=input("Please Enter the Customer Email Id :")
    regex12 = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    valid12=re.match(regex12,email)
    if valid12:
        class Tea:
            def price_tea(self):
                self.tea_price=7
                return self.tea_price
        class Coffee:
            def price_coffee(self):
                self.coffe_price=10 
                return self.coffe_price
        class Masala_Dosa:
            def price_dosa(self):
                self.dosa_price=50
                return self.dosa_price

        class Bill_Order(Coffee,Tea,Masala_Dosa):
            pass

        billing=Bill_Order()
        price=0

        while(True):

            print("\nSelect an option from menu ")
            print("\n")
            print("1. Tea (Rs.7)")
            print("2. Coffee (Rs.10)")
            print("3. Masala Dosa (Rs.50)")
            print("4. View Bill and Email ")
            choice=int(input("Enter your Order choice: "))
            if choice==1:
                print("\nTea selected")
                teaprice=billing.price_tea()
                price+=teaprice
            if choice==2:
                print("\nCoffee selected")
                coffeeprice=billing.price_coffee()
                price+=coffeeprice
            if choice==3:
                print("\nMasala Dosa Selected")
                dosaprice=billing.price_dosa()
                price+=dosaprice
            if choice==4:
                print("Your Bill ")
                print("RS",price)
                price=str(price)
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
                connection.sendmail("priya.hajela358@gmail.com",email,price)

                print("Email for your bill successfully sent")
                connection.quit()
                break
        break          
    else:
        print("Please Enter a valid Email ID")
        continue
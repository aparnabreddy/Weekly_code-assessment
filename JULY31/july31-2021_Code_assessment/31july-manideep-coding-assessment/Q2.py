import re
import smtplib
while(True):
    Name=input("Please Enter your Name :")
    Email=input("Please Enter the Email Id :")
    regex = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    validation=re.match(regex,Email)
    if validation:
        class Tea:
            def price_tea(self):
                self.tea_p=7
                return self.tea_p

        class Coffee:
            def price_coffee(self):
                self.coffe_p=10 
                return self.coffe_p
        
        class Masala_Dosa:
            def price_dosa(self):
                self.dosa_p=50
                return self.dosa_p




        class Bill_Order(Coffee,Tea,Masala_Dosa):
            pass


        bill=Bill_Order()
        cost=0

        while(True):

            print("\nSelect an option from menu ")
            print("\n")
            print("1. Tea (Rs.7)")
            print("2. Coffee (Rs.10)")
            print("3. Masala Dosa (Rs.50)")
            print("4. View Bill and Email ")
            choice=int(input("\nEnter your Order choice:"))
            


            if choice==1:
                print("\nTea selected")
                tea1=bill.price_tea()
                cost+=tea1
                    

            if choice==2:
                print("\nCoffee selected")
                cof1=bill.price_coffee()
                cost+=cof1
            

            if choice==3:
                print("\nMasala Dosa Selected")
                dosa1=bill.price_dosa()
                cost+=dosa1
                
            if choice==4:
                print("Your Bill ")
                print("RS",cost)
                message=str(cost)
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("manideepkotha324@gmail.com","mani@9324")
                connection.sendmail("manideeokotha324@gmail.com",Email,message)

                print("Email for your Bill has successfully send")
                connection.quit()
                break
        break          
    else:
        print("Please Enter valid Email ID")
        continue
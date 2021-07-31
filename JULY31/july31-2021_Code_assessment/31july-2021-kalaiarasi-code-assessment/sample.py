class menu:
    def tea(self,a):
        return a*7
    def coffee(self,b):
        return b*10
    def masaladosa(self,c):
        return c*50
c=menu()
bill=0
while(True):
    print("select an option:")
    print("\n")
    print("1.tea            - RS:7")
    print("2.coffee         -RS:10")
    print("3.masaladosa     -RS:50")
    print("4.View Bill and Email")
    choice=int(input("enter ur choice:"))
    #a=int(input("enter a"))
    #b=int(input("enter b"))
    if choice==1:
        print("tea selected")
        a=int(input("enter count of tea:"))
        #b=int(input("enter b:"))
        #print("sum",c.add(a,b))
        ans=c.tea(a)
        bill=bill+ans

    if choice==2:
        print("coffee selected")
        b=int(input("enter count of coffee:"))
        #b=int(input("enter b:"))
        #print("sub",c.sub(a,b))
        ans=c.coffee(b)
        bill=bill+ans
    if choice==3:
        print("masala dosa selected")
        c=int(input("enter count of masaladosa:"))
        #b=int(input("enter b:"))
        #print("sub",c.sub(a,b))
        ans=c.masaladosa(c)
        bill=bill+ans
       
    if choice==4:
        break
print(bill)
message=str(bill)
import smtplib
connection =smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("kalai.iprimed@gmail.com","Kalai@2404")
connection.sendmail("kalai.iprimed@gmail.com","pkalai2404@gmail.com",message)
print("email send")
connection.quit()



a=int(input("enter the number:"))
e=[]
o=[]
def check(x):
    if(x%2==0):
        e.append(x)
       
    else:
        o.append(x) 
       
check(a)           
print(o)
print(e)
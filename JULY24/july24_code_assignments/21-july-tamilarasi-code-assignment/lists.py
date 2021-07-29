n1=int(input("Enter the Num:"))
even=[]
odd=[]
def check(n1):
    if(n1%2==0):
        even.append(n1)
    else:
        odd.append(n1)
check(n1)
print(even)
print(odd)
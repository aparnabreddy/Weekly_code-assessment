even=[]
odd=[]
num1=int(input("enter the number"))
def check(a):
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
check(num1)
print(even)
print(odd)
x=int(input("enter the no"))
even=[]
odd=[]
def check(x):
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
check(x)
print(even)
print(odd)

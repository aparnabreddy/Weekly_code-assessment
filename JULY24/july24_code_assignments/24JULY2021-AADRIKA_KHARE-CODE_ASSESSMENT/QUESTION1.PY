even=[]
odd=[]
n=int(input("Enter a number:"))

def check(a):
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
check(n)
print(even)
print(odd)
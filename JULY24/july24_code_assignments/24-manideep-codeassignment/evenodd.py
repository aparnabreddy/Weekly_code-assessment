n1=int(input("enter a number : "))
even=[]
odd=[]
def evenodd(n1):
    if(n1%2==0):
        print(n1,"even number")
        even.append(n1)
    else:
        print(n1,"odd number")
        odd.append(n1)
evenodd(n1)
print(even)
print(odd)
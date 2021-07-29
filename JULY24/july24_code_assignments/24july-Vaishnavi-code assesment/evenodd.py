num=int(input("Enter a number : "))
even=[]
odd=[]
def evenOdd(num):
    if(num%2==0):
        even.append(num)
    else:
        odd.append(num)
evenOdd(num)
print(even)
print(odd)
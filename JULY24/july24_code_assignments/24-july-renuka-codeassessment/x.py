evenlist=[]
oddlist=[]
n=int(input("enter a number"))
def evenOdd(n):
    if(n%2==0):
        evenlist.append(n)
    else:
        oddlist.append(n)
evenOdd(n)
print(evenlist)
print(oddlist)


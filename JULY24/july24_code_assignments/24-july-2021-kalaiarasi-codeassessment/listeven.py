n=int(input("enter the num:"))
even=[]
odd=[]
def check(n):
        if(n%2==0):
            even.append(n)
        else:
            odd.append(n)
check(n)
print("even:",even)
print("odd:",odd)

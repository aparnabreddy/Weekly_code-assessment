odd=[]
even=[]
def check(n):
    if n%2==0:
        even.append(n)  
    else:
        odd.append(n)   
n=int(input("Enter a number: "))
check(n)
print("evenlist: ",even)
print("oddlist: ",odd)
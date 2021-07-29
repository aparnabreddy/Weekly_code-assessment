even=[]
odd=[]
def check(x):
    if a%2 == 0:
        even.append(a)
    else:
        odd.append(a)

a=(int(input("Give a value:")))

check(a)
print(even)
print(odd)


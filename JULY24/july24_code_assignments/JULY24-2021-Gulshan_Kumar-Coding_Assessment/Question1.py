num = int(input('enter the number'))
even =[]
odd = []
def check(num):
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
check(num)
print(even,"is even")
print(odd,"is odd")
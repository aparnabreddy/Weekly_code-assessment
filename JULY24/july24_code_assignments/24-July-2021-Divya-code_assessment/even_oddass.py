def check(a):
    if (num%2==0):
        even.append(num)
        print("yes,it is even number: ",num)
    else:
        odd.append(num)
        print("yes,it is odd number: ",num)
num = int(input("Enter a number: "))
even = []
odd = []
check(num)

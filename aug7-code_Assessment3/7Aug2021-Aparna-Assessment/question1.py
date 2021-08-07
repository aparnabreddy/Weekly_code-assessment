import multiprocessing,logging

list_of_numbers=[]
even=[]
odd=[]

# ---function to print even numbers---
def printEven(getlist):
    for i in getlist:
        if(i%2==0):
            even.append(i)
    print("even numbers are:" ,even)

# ---function to print odd numbers---
def printOdd(getlist):
    for j in getlist:
        if(j%2!=0):
            odd.append(j)
    print("Odd numbers are: ",odd)
# list_of_numbers=[1,2,3,4,5,6,7,8,9] #user defined list

if(__name__=='__main__'):
# ----getting list of numbers from user-----
    try:
        n=int(input("Enter the size of the list: "))
        print("Enter the" ,n ,"numbers")
        for i in range(0,n):
            number=int(input())
            list_of_numbers.append(number)
    except ValueError:
        logging.error("please enter integer numbers ")

    p1=multiprocessing.Process(target=printEven,args=(list_of_numbers,))  
    p2=multiprocessing.Process(target=printOdd,args=(list_of_numbers,))  
    p1.start()
    p2.start()
    p1.join()
    p2.join()


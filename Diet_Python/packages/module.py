def isLeapYear(year):
    if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        print("Leap")
    else:
        print("Not a Leap")
        
        
def add(n1,n2):
    return n1+n2

def isPrime(num):
    flag = 0
    for i in range(2,num):
        if num%i == 0:
            flag = 1
    if flag == 1:
        print("Not a Prime")
    else:
        print("Prime")
        
# Print all even numbers with in given boundaries
def allEven(lb,ub):
    for i in range(lb,ub+1):
        if i%2 == 0:
            print(i)
            
            
# write a python code for factorial of a number
def fact(number):
    mul =1
    for i in range(1,number+1):
        mul *= i 
    return mul
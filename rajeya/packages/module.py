def add(num1,num2):
    return num1+num2

def isleapyear(year):
    if year%400==0:
        print("it is a leap year")
    else:
        print("it is not a leap year")
        
def add(n1,n2):
    return n1+n2

def isprime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
    if flag==1:
          print("not a prime")
    else:
          print("prime")
            
# print all even numbers within given boundaries
def alleven(lb,ub):
    for i in range(lb,ub+1):
        if i%2==0:
            print(i)
            
def fact(number):
    mul=1
    for i in range(1,number+1):
        mul *= i
        return mul
    
# write a code for special    
        
    
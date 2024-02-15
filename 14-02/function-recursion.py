# Factorial : 5
#               5 * 4 * 3 * 2 * 1
n = int(input("Enter the number:- "))

def factorial(n):
    if(n ==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
outputxt = "Factorial of {0} is : {1} "
print(outputxt.format(n,factorial(n)))
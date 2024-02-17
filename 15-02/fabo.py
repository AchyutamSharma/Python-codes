# fibonacci series 

user_input = int(input("Enter the number for fibonacci series:- "))

def fibonacci(user_input):
    a = 0
    b = 1
    if user_input<0:
        return "Invalid input"
    elif user_input ==0:
        return a
    elif user_input == 1:
        return b
    else:
        for i in range(1,user_input+1):
            c = a + b
            a = b 
            b = c
            print(i,b)
        return b

print("Fibonacci of",user_input,"is",fibonacci(user_input))
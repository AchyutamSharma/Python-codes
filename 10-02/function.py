
x = int(input("Enter the First value: - "))
y = int(input("Enter the Second value: - "))


def Multiple(firstVal,secondVal):
    if(firstVal != 0):
        finalVal = firstVal*secondVal
        print("Your Final output =",finalVal)
    else:
        print("You Enter 0.. Please try again")


Multiple(x,y)
   

# If you need to skip or write this function after some time we need to write 'pass' inside the func()
# then it cant show the error
def Skipfucntion():
    pass


userinput = int(input("Enter the number:- "))
print("Your input is",userinput)
if(userinput < 0):
    print("It is a negative number.")
elif(userinput == 0) :
    print("Its is 0.")
elif(userinput > 0):
     if(userinput > 0 and userinput <= 30):
        print("Its is positive number and between 0 to 30")
     elif(userinput > 31 and userinput <= 60):
        print("Its is positive number and between 31 to 60")
     else:
        print("Its is positive number and between 61 to 100")
else:
    print("Wrong Input")


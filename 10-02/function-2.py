
x = int(input("Enter the First value: - "))
y = int(input("Enter the Second value: - "))


def greaterThan(firstVal,secondVal):
    if(firstVal > secondVal):
        print(firstVal,"is greater than",secondVal)
    elif(firstVal == secondVal):
        print(firstVal,'is Equal to',secondVal)
    else :
        print(firstVal,"is less than",secondVal)

def Add(firstVal,secondVal):
    print(firstVal,'+',secondVal,'=',firstVal+secondVal)

def subtract(firstVal,secondVal):
    print(firstVal,'-',secondVal,'=',firstVal-secondVal)

def modulos(firstVal,secondVal):
    print(firstVal,'%',secondVal,'=',firstVal%secondVal)


if(x > 0 and y > 0):    
    greaterThan(x,y)
    Add(x,y)
    subtract(x,y)
    modulos(x,y)
elif(x<0 and y<0):
    print("Enter the valid number which is not Negative")
else:
    print("Enter the valid number which is not 0 or start with  0 ")

userInput = input("Enter the 'yes' or 'no' for enter to our wb: ")

match userInput:
    case 'yes' :
        print("Welcome to our Website.")
        user_Age = int(input("Please Enter Your Age:- "))
        if (user_Age >= 18):
            print("Your Age is valid to our website....")
        else:
            print("You are under age..., Please Exit")    
    case 'no':
        print("Thankyou, Come again..")
    case _: 
        print("Enter the valid input.")
        

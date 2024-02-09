
user_name = input("Enter Your Name: ")
if(user_name.isalpha() is True):
    for out in user_name:
        print(out)
        if(out == 'o'):
            print("You name is unique ('o') - you win Reward")
else:
    print("\t\tYou Enter the Number....")
    print("\t\tPlease try again....")

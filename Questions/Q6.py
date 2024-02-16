# Check if a Password is 'weak', 'Medium' or 'strong'. 
# Criteria: < 6 chars (weak), 6-10 chars(Medium), > 10 chars (Strong).

user_password = input("Enter your password: ")

pass_length = len(user_password)

if(pass_length < 6):
    print("Your Password is too weak!!!!.")
elif(pass_length >= 6 and pass_length < 10):
    print("Your Password is Medium!!. We suggest to change it.")
elif(pass_length >=10 and pass_length<=25):
    print("Hey!!!\n You need to chill.\n Your Password is Strong!!.")
else:
    print("Invalid Input...\n Please Try-Again...")
    print(" Reason:- Your Password is too long please write a valid password.")
print(pass_length)
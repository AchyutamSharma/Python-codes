#       chai or code Question - 1


user_input = int(input("Enter the Age :- "))

if(user_input > 0 and user_input <= 13):
    print("You are a child.")
elif(user_input >= 14 and user_input <= 19):
    print("You are Teenager.")
elif(user_input >= 20 and user_input <= 59):
    print("You are Adult.")
elif(user_input >= 60 and user_input <= 120):
    print("You are Senior.")
else:
    print("Enter the right value.")
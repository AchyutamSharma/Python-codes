# Determine if a fruit is ripe, overripe, or unripe based on its color.
#  (e.g.- Banana: Green - Unripe,Yellow - Ripe, Brown - Overripe)


user_fruits =  input("Enter the Name of your Fruits:- ")
user_color =  input("Enter the color of your Fruits:-  ")

output_txt = 'Your {0} is {1} now'

if(user_color == "Green" or user_color == "green"):
    green = 'Unripe'
    print(output_txt.format(user_fruits,green))
elif(user_color == "Yellow" or user_color == "yellow"):
    yellow = 'Ripe'
    print(output_txt.format(user_fruits,yellow))
elif(user_color == "Brown" or user_color == "brown"):
    brown = 'Overripe'
    print(output_txt.format(user_fruits,brown))
else:
    print("Enter the valid input.")

# Weather Activity Suggestion:- Suggestion an activity based on the weather
#   e.g.- Sunny-'go for walk', Rainy -'Read a Book', Snowy - 'Build a Snowman'.


list = ['1. Sunny Day','2. Rainy Day','3. Snowy Day']

for i in list:
    print(i)

user_input = int(input("Enter the weather number of above lists:- "))

if(user_input == 1):
    print("You can 'Go for Walk'")
elif(user_input == 2):
    print("You can 'Read' a Book!! ")
elif(user_input == 3):
    print("You can Build a 'Snowman'.")
else:
    print("Enter the Valid Input.")

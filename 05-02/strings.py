


#                Single line String

# Firstname = str(input("Enter your First name:- "))
# lastname = str(input("Enter your Last name:- "))
# print("Hello, ",Firstname+ " " +lastname)

#               Multi-line string

UserData = """You can use three "double" quotes 
Or 
three 'single' quotes """

print(UserData)

#              Accessing Characters of a String
print(UserData[2]) # output- u

print("Lets use loop in String.\n")
#               for-in loop 
for SepratedData in UserData:
    print(SepratedData)

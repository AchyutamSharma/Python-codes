userName = input("Enter your name :- ")
userinput = int(input("Enter your Age :- "))

print("Hello ",userName)
print("\tYour Age is",userinput)

if(userinput >= 18 and userinput <= 60) :
    print("\t\t",userName,"you can Drive..")
elif(userinput >= 61 ) :
    print("\t\tSir",userName,"you are too old. Please drive carefuly....")
elif(userinput<18):
    print("\t\t",userName,"you can't Drive")
else:
    print("\t\tWrong Input")
'''
print("You need to give space to 'print' after 'if' or 'else'.")
'''    


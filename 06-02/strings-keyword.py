
greeting = "Hello " 
about = "today We Start String Methods !!!!!"
_userName = "Lily "
name = "Harry"


print(len(about))

print( greeting + _userName.upper() + "," + about.lower())

print(about.lower().rstrip("!"))

print(_userName.replace("Lily","Akshutam"))

z = about.split(" ")
print(z)

blog = "hello this is Introduce Js and Python"
print(blog.capitalize())

print(name.center(50))
print("Length of Name after using center = ",len(name.center(50)))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!")) #true
print(str1.endswith("H")) #false
print(str1.endswith("to",4,10)) #true

str2 = "He's name is Akshutam. He is an honest man."
print(str2.find("is")) #10 index
str2 = "His name is Akshutam. He is an honest man."
print(str2.find("is")) #1 index 
str2 = "His name is Akshutam. He is an honest man."
print(str2.find("iss")) #-1 index because word does not exitis 

# print(str2.index("iss")) # it throw the error 
print(str2.index("is")) # it show the first index of "is"

str = "Welcome To The Our Website"
print("This is 'isalnum() = '",str.isalnum()) # false
str = "WelcomeToTheOurWebsite"
print("This is 'isalnum() = '",str.isalnum()) #true
str = "WelcomeToTheOurWebsite007"
print("This is 'isalnum() = '",str.isalnum()) #true

addnum = "Hello This is 007"
print("\nThis is 'isalpha() = '",addnum.isalpha()) # false
addnum = "Hello Its Akshutam"
print("This is 'isalpha() = '",addnum.isalpha()) # false
addnum = "HelloItsAkshutam"
print("This is 'isalpha()' = ",addnum.isalpha()) # True

txt =  "Hello"
print("\nThis is 'islower()' =",txt.islower()) # false
txt =  "hello"
print("This is 'islower()' =",txt.islower()) # true

txto = "\nThis is example of printable "
print("\nThis is 'isprintable()' = ",txto.isprintable()) # false - because we use '\n' 
txto = "This is example of printable "
print("This is 'isprintable()' = ",txto.isprintable())

space = "    " #using spacebar
print("\nThis is 'isspace()' = ",space.isspace())
space = "       " #using Tab
print("This is 'isspace()' = ",space.isspace())
space = "       007" #using Tab + num
print("This is 'isspace()' = ",space.isspace()) # false - we use num that why

title = "weLcome to our place"
print("\nThis is .title() = ",title.title()) #it automaticaly change to upperCase 
title = "welcome to our place"
print("This is .title() = ",title.title()) #it automaticaly change to upperCase 

InTitle = title.title()
print("\nThis is after title use = ",InTitle)
print("This is 'istitle()' =", InTitle.istitle()) # true - Its show the it is in title form 

inCenter = "This is add space and center it"
centers = inCenter.center(50)
print("\n",centers)
print("The length of center = ",len(centers))

word  = "Python is really easy lang."
print("\n This is .startswith() = ",word.startswith("P"))
print(" This is .startswith('Python') = ",word.startswith("Python"))
print(" This is .startswith('y') = ",word.startswith("y"))

print("\nThis is endswith('.') = ", word.endswith("."))
print("This is endswith('No') = ", word.endswith("No"))

print("\nThis is swapcase() = ",word.swapcase()) # it change to lower to upper and upper to lower


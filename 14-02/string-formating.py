

str1 = "Hello"
str2 = "World"
str3 = str1 + " " + str2
print(str3)

txt = "This is the way of {} formating.{}"
print(txt.format("String","!!"))

# x = input(txt.format("'String'"))
# print(x)
'''
user_name = input("Enter your name : ")
user_age = input("Enter your Age : ")
user_dob = input("Enter your DOB : ")
txt2 = "Hello, {0}. \nYour Age :{1}\nDate of birth:{2}"
afterAdd = txt2.format(user_name,user_age,user_dob)
print(afterAdd)
'''

buySome = "I wanna buy {0},but my buget is{price: .2f}$,Do you have {card}??"
print(buySome.format("apple watch", price = 100.9555,card="Credit Card"))

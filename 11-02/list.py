
listitmes = ['hello', 'bro',3,2001.08,12]
color = ['red','blue','yellow','black','white']
# print(listitmes)

# for i in listitmes:
#     print(i)
# print(listitmes)
# print(listitmes[-3])

user_input = input("Enter the color name:- ")

if user_input in color:
    print("Yes, we have",user_input,"color")
else:
    print("No we dont have.")
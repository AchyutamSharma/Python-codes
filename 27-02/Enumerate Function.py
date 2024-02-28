
fruits = ['apple','banana','kiwi','oranges']
Questions = ('What is your name?','What is your Age?','Where do you live?')

for idx,val in enumerate(fruits):
    print(idx+1,val)

print("")
#  This is also a method that was do same thing as above. 
# index = 0
# for val in fruits:
#     index+=1
#     print(index,val)

for i, data in enumerate(Questions):
    print(i+1,"-",data)
    if(i == 1):
        print("Btw,")
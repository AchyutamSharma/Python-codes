
Question = [
    [
        "The World Largest desert is ? ", " Thar"," Kalahari"," Sonoran"," Sahara" ,"None", 4
    ],
    [
        "The World Largest Forest is ? ", " SundarVan"," Ghar ke pass wala"," Sahara nahi hai"," Amazon","None",4
    ],
    [
        "The World Largest desert is ? ", " Thar"," Kalahari"," Sonoran"," Sahara" ,"None", 4
    ],
    [
        "The World Largest desert is ? ", " Thar"," Kalahari"," Sonoran"," Sahara" ,"None", 4
    ],
    [
        "The World Largest desert is ? ", " Thar"," Kalahari"," Sonoran"," Sahara" ,"None", 4
    ],

]

level = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0
for i in range(0,len(Question)):
    questions = Question[i]
    print("Level of Rs",level[i])
    print(questions[i])
    print(f"1.{questions[1]}        2.{questions[2]}")
    print(f"3.{questions[3]}        4.{questions[4]}")
    reply = int(input("Enter your Answer (1-4) "))
    if (reply == questions[-1]):
        print(f"Correct Answer, you have won Rs{level[i]}")
        if(i == 4):
            money = 10000
            print(f"your winning amount rs{money}")
        elif(i == 9):
            money = 320000
            print(f"your winning amount rs{money}")
    else:
        print("Wrong Answer.")
        print(f"your winning amount rs{money}")    
        break



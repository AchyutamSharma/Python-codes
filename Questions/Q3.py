# Grade Calculator
#   Assign a letter grade based on student's score :
#       A+(90-100) A(85-89) A-(80-84) B+(75-79) B(70-74) C+(65-69) C(60-64) D+(55-59)  
#       D(50-54) E(40-49)  F(0-39)


def gradeChecker(marks):
    if((marks>=90) and (marks<=100)):
        print("Your marks is",marks," Score A+ Grade")
    elif((marks>=85) and (marks<=89)):
        print("Your marks is",marks," Score A Grade")
    elif((marks>=80) and (marks<=84)):
        print("Your marks is",marks," Score A- Grade")
    elif((marks>=75) and (marks<=79)):
        print("Your marks is",marks," Score B+ Grade")
    elif((marks>=70) and (marks<=74)):
        print("Your marks is",marks," Score B Grade")
    elif((marks>=65) and (marks<=69)):
        print("Your marks is",marks," Score C+ Grade")
    elif((marks>=60) and (marks<=64)):
        print("Your marks is",marks," Score C Grade")
    elif((marks>=55) and (marks<=59)):
        print("Your marks is",marks," Score D+ Grade")
    elif((marks>=50) and (marks<=54)):
        print("Your marks is",marks," Score D Grade")
    elif((marks>=40) and (marks<=49)):
        print("Your marks is",marks," Score E Grade")
    elif((marks>=0) and (marks<=39)):
        print("Your marks is",marks," Score F Grade")
    else:
        print("Wrong Input... Please Try Again")

list = []

def addsub():
    for i in range(subjects):
        user_input = int(input ('Enter your subjects marks :-'))
        list.append(user_input)
    for i in list:
        gradeChecker(i)
    
def avgMarks():
    total = 0
    for n in list:
        total+= n
    avg = total/len(list)
    return avg

subjects = int(input("How many subject do you have? :- "))
if (subjects >= 2) : 
    addsub() 
    total_marks = avgMarks()
    print("Your Average marks :",total_marks)   
elif (subjects==1):
    marks = int(input("Enter your marks:- "))
    gradeChecker(marks)
else: print("Wrong input")        
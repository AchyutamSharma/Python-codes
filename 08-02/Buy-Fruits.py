
arr = ['apple','banana', 'kiwi','gauva','papaya','Mango','Avacado']

satis = "Are you satisfy with this rate? (yes or no) :-"
want_txt = "How many kg you want?? (type 1kg for 1 or 500g for 0.5):-"

user_input = input("Do you wanna buy fruits ? ('yes' or 'no') :- ")

if(user_input == 'yes'):
    print("We have this fruits")
    for fruits_name in arr:
        print(fruits_name.capitalize()," ")

    user_input_2 = input("We have this fruit. Do you wanna buy this fruits ? ('yes' or 'no') :- ")
    if(user_input_2 == 'yes'):
        select_fruit = input("Give the name of a fruits in the above list :-")
        if(select_fruit.isalpha() == True):
            match select_fruit:
                case 'Apple'|'apple':
                    price = 200
                    mrp = price + (price/100)*20
                    print("You Select Apple :- ","\n\tMRP :",mrp,"/kg\n\t Rate:",price,"/kg")
                    satisfy = input(satis)
                    if(satisfy == 'yes'):
                        user_want = int(input(want_txt))
                        rate = user_want * price
                        print("\t\tMRP:",mrp,"\n\t\tPrice :",price,"\n\t\tQuantity :",user_want,"\n\t\tTotal =",rate)
                    else:
                        print("Thankyou Come Again :)")
                
                case 'banana'|'Banana':
                    price = 30
                    mrp = price + (price/100)*20
                    print("You Select Banana :- ","\n\tMRP :",mrp,"/kg\n\t Rate:",price,"/kg")
                    satisfy = input(satis)
                    if(satisfy == 'yes'):
                        user_want = int(input(want_txt))
                        rate = user_want * price
                        print("\t\tMRP:",mrp,"\n\t\tPrice :",price,"\n\t\tQuantity :",user_want,"\n\t\tTotal =",rate)
                    else:
                        print("Thankyou Come Again :)")
                
                case 'Kiwi'|'kiwi':
                    price = 250
                    mrp = price + (price/100)*20
                    print("You Select Kiwi :- ","\n\tMRP :",mrp,"/kg\n\t Rate:",price,"/kg")
                    satisfy = input(satis)
                    if(satisfy == 'yes'):
                        user_want = int(input(want_txt))
                        rate = user_want * price
                        print("\t\tMRP:",mrp,"\n\t\tPrice :",price,"\n\t\tQuantity :",user_want,"\n\t\tTotal =",rate)
                    else:
                        print("Thankyou Come Again :)")
                
                case 'Guava'|'guava':
                    price = 60
                    mrp = price + (price/100)*20
                    print("You Select Kiwi :- ","\n\tMRP :",mrp,"/kg\n\t Rate:",price,"/kg")
                    satisfy = input(satis)
                    if(satisfy == 'yes'):
                        user_want = int(input(want_txt))
                        rate = user_want * price
                        print("\t\tMRP:",mrp,"\n\t\tPrice :",price,"\n\t\tQuantity :",user_want,"\n\t\tTotal =",rate)
                    else:
                        print("Thankyou Come Again :)")

                case 'Papaya'|'papaya':
                    price = 80
                    mrp = price + (price/100)*20
                    print("You Select Papaya :- ","\n\tMRP :",mrp,"/kg\n\t Rate:",price,"/kg")
                    satisfy = input(satis)
                    if(satisfy == 'yes'):
                        user_want = int(input(want_txt))
                        rate = user_want * price
                        print("\t\tMRP:",mrp,"\n\t\tPrice :",price,"\n\t\tQuantity :",user_want,"\n\t\tTotal =",rate)
                    else:
                        print("Thankyou Come Again :)")

                case 'Mango'|'mango':
                    price = 130
                    mrp = price + (price/100)*20
                    print("You Select Mango :- ","\n\tMRP :",mrp,"/kg\n\t Rate:",price,"/kg")
                    satisfy = input(satis)
                    if(satisfy == 'yes'):
                        user_want = int(input(want_txt))
                        rate = user_want * price
                        print("\t\tMRP:",mrp,"\n\t\tPrice :",price,"\n\t\tQuantity :",user_want,"\n\t\tTotal =",rate)
                    else:
                        print("Thankyou Come Again :)")


                case 'Avacado'|'avacado':
                    price = 300
                    mrp = price + (price/100)*20
                    print("You Select Avacado :- ","\n\tMRP :",mrp,"/kg\n\t Rate:",price,"/kg")
                    satisfy = input(satis)
                    if(satisfy == 'yes'):
                        user_want = int(input(want_txt))
                        rate = user_want * price
                        print("\t\tMRP:",mrp,"\n\t\tPrice :",price,"\n\t\tQuantity :",user_want,"\n\t\tTotal =",rate)
                    else:
                        print("Thankyou Come Again :)")
                case _:
                    print("Wrong Input...")
        else:
            print("Wrong Input...\nPlease try again...")
    else:
        print("Please come again.....")
else:
    print("Please come again.....")

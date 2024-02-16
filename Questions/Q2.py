# Movie ticket pricing
# Movie ticket pricing based on age : $12 for adults(18 or over), $8 for children. Everyone gets $2 discount on wednesday.


age = int(input("Enter your age :- "))
qty = int(input("How many tickets do you want ?? "))

def ticket(age,qty):
    days = "friday" #"wednesday"
    price = 12 if age>=18 else 8
    if  days == "wednesday":
        price -= 2

    totalprice  = qty * price

    print('Quantity : ',qty,'Price :',price)
    print('Your Total Ticket price is $',totalprice)

ticket(age,qty)
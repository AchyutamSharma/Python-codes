

a = int(input("Enter the number of 'A' :- "))
b = int(input("Enter the number of 'B' :- "))

print("A is greater") if a>b else print("A = B") if a==b else print("B is Greater then A")


c = a + b 
print(c) if a==b else print(a," > ",b) if a>b else print(a,"<",b)

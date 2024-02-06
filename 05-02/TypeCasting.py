# Date 05-02-2024
# Day 2 of 60days of code Python

print("\n\t\t------Explicit TypeCasting-----")
a = 10
b = "20"

#                           This is Explicit TypeCasting
print(type(a),type(b))

'''
print(a+b) -> It show the error - 'int' and 'str'.  
    You need to Change to int.
'''    

print(a + int(b))        
#output - 30
print(type(int(b))) #It change into integer form

#                           This is Implicit TypeCasting
print("\n\t\t------Implicit TypeCasting-----")
x = 10.9
y = 20

z = x+y

print("Type of x = ",type(x),"\nType of y = ",type(y),"\n",x," + ",y," = ",z,"\nType of z = ",type(z))



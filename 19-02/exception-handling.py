
# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")

# try: 
#     for i in range(1,11):
#         print(f"{int(a)} x {i} = {int(a) * i}")
# except:
#     print("Invalid Input")



try: 
    num = int(input("Enter the number: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Invalid Input. The number is not a Integer.")

except IndexError:
    print("Invalid Input. Index-Error")

print("This is last line.")


try: 
    num = int(input("Enter the number: "))
    a = [6,3]
    print(a[num])
except Exception as e:
    print("Invalid Input :- ",e)
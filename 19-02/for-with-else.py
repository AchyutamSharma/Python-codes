

for i in range(1,5):
    print(i)
else:
    print("The 5th count is ended...")



for i in []:
    print(i)
else:
    print("This is empty set...")


n = int(input("Enter the number:- "))

for i in range(1,n):
    print(i)
    if i== 5:
        break
else:
    print("The 5th count is ended. But it don't print this line because of break keyword...")

print('\n\t\t-------While()-------\n')
# same goes with the While() loop
i = 0
while(i<n):
    print(i)
    i+=1
    # if i== 5:
    #     break
else:
    print("The 5th count is ended. But it don't print this line because of break keyword...")

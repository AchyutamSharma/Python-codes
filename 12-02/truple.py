

# Truple 

truple1 = (1,2,3,4,5,6,7,8,'hello')

print(truple1)

# for i in truple1:
#     print(i)

# truple1[0] = 10 Error show 

tup = ("apple","orange","kiwi","banana","stawbarry")
# for i in tup:
    # print(i)
newone = truple1 + tup
print(newone)

print("This is Negative index:- ",newone[-9:-1])
print("This is Negative index with skipValue:- ",newone[-9:-1:2])

print("This is Positive index :- ",newone[:6])
print("This is Positive index with skipValue:- ",newone[:6:2])



if "orange" in tup:
    print("Yes, we have orange.")
else:
    print("No, we dont have.")


contry = ("Spain","Itly","Bharat","USA","Germany")

"""
We can't change data of truple. 
make a new variable and convert to list then store in that variable. """

temp = list(contry)
print("It convert to list :- ",temp)

temp.append("Russia")
print(temp)

temp.pop(1) # remove data
print(temp)

#change data
temp[0] = "Itly"
print(temp)

contry = tuple(temp)
print("After add in tuple :",contry)


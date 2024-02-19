
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])# it show the full error 
print(info.get('eligible'))# it show the None

#   Accessing value :-
r001 = {'name':'Akshutam Sharma','Age':23,'Passout':2023,'CGPA':7}
print(r001.values())

#   Accessing key:-
r002 = {'name':'Deven Sharma','Age':22,'Passout':2023,'CGPA':8}
print(r002.keys())

#   Accessing key-value pairs:-
r003 = {'name':'Ebenizer Gladwin','Age':23,'Passout':2023,'CGPA':9}
print(r003.items())

#   Create a new key and assign a value to it
r004 = {'name':'Lavanya Bai','Age':21,'Passout':2023,'CGPA':7.5}
r004['DOB'] = 2002
print(r004)

#   Use the update() method:
r005 = {'name':'Diya Roy','Age':21,'Passout':2023,'CGPA':6.5}
print(r005)
r005.update({'Age':22})
r005.update({'DOB':2001})
print(r005)



#Removing items from dictionary
rclean = {'name':'Diya Roy','Age':21,'Passout':2023,'CGPA':6.5}
rclean.clear()
print("This is clean() :-",rclean)


#   pop(): The pop() method removes the key-value pair whose key is passed as a parameter.
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('age')
print("This is pop() =",info)


#   popitem(): The popitem() method removes the last key-value pair from the dictionary.
info = {'name':'Karan', 'age':19, 'eligible':True}
info.popitem()
print("This is popitems() = ",info)

# del keyword to remove a dictionary item. 
info1 = {'name':'Karan', 'age':19, 'eligible':True}
del info1['age']
print("This is 'del' = ",info1)


#   copy() method to copy the contents of one dictionary into another dictionary.
arr = {'name': 'binod','age': 'unknow','Kaam':'memer'}
newArr = arr.copy()
print("This is copy() -new Array =",newArr)


#   dict() function to make a new dictionary with the items of original dictionary.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
newDic = dict(info)
print("This is dict :-",newDic)

#

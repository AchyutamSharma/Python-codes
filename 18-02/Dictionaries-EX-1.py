r001 = {'name':'Akshutam Sharma','Age':23,'Passout':2023,'CGPA':7}
r002 = {'name':'Deven Sharma','Age':22,'Passout':2023,'CGPA':8}
r003 = {'name':'Ebenizer Gladwin','Age':23,'Passout':2023,'CGPA':9}
r004 = {'name':'Lavanya Bai','Age':21,'Passout':2023,'CGPA':7.5}
r005 = {'name':'Diya Roy','Age':21,'Passout':2023,'CGPA':6.5}

x = [r001,r002,r003,r004,r005]
i = 0
for z in range(len(x)):
    for key, value in x[z].items():
        print(f"{key} :- {value}")
        # x[i+1]
    print("\n-------------\n")    

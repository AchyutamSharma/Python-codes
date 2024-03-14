
# f = open("myfile.txt",'r')

# while True:
#     line =f.readline()
#     if not line:
#         break
#     print(line)




#  Its make a new file and write txt 
f = open('myfile2.txt','w')
line = ['line 1\n','line 2\n','line 3\n']
f.writelines(line)
f.close()

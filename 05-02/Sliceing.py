
#     Slice Methods


name = "Fastrack"
name1 = "Hellcat"

print(name,"=",len(name),name1,"=",len(name1))
print(name[0:5])
print(name[0:-3])# name[0: len(name)-3] = {len(name)-3} = {8-3=5} = name[0:5] 
print(name[:-3]) # by-default it take 0.
print(name1[-1:-4])#name1[len(name1)-1:len(name1)-4] ={(7-1):(7-4)} =name1[6:3]-Starting from 6 to 3. I not print output.
print(name1[-4:-1])#name1[len(name1)-4:len(name1)-1] ={(7-4):(7-1)} =name1[3:6]- Output = lca. Starting from 3 to 6.


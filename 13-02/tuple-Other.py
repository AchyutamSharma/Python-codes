tups = (1,2,3,4,5,6,7,8,9,10,11,12,3,1,2,3)

res = tups.count(1)
print("This is .count(1) =",res)

idx = tups.index(10)
print("This is index(10) =",idx)


tups2 = (1,2,3,4,3,1,2,3)
print("Length = ",len(tups2))
advIdx = tups2.index(3,3,7)
print("This is index( number, start, end) of 3 = ",advIdx)


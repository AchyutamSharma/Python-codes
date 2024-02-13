
items = [11,1,200,201,302,1,99,2,9,10,5,4,3,101,1]

print("Before append() =",items)
items.append(6)
print("After append() =",items)

items.reverse()
print("This is reverse() = ",items)

items.sort()
print("This is sort() =",items)

items.sort(reverse=True)
print("This is sort(reverse=True) =",items)

print("This is index() of 10 = ",items.index(10))

counts = items.count(1)
print("This is count() of 1 =",counts)

copyItems = items.copy()
copyItems[0] = 402
print("This is use of copy() =",copyItems)

items.insert(1,2000)
print("This is 'insert( index , value of insert)' =",items)

#   This is concatination of newitmes and items

newItems = [1001,1002,3003]
updatedlist = items + newItems
print("This is concatination of items and newItems =",updatedlist)

# One more method is extends() it add in old list

items.extend(newItems)
print("This is extend() =",items)


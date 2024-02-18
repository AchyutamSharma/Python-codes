
'''            Union():-  union can make a new variable of set and it don't change the old variable        '''

cities1 = {'delhi','noida','bengaluru','mumbai'}
cities2 = {'kolkata','chenai','kochi','mumbai','noida'}
print(cities1,cities2)

Union_cities = cities1.union(cities2)
print("After Union():- ",Union_cities)


'''          update():-  update can change the main variable of set                '''


city1 = {'delhi','noida','bengaluru','mumbai'}
city2 = {'kolkata','chenai','kochi','mumbai','noida'}

city1.update(city2)
print("After update() can add two set:- ",city1)


'''               intersection():- it show the value of set which is present in both set         '''


city1 = {'delhi','noida','bengaluru','mumbai'}
city2 = {'kolkata','chenai','kochi','mumbai','noida'}
intersect_city3 = city1.intersection(city2)
print(".intersection() :- ",intersect_city3)


'''           intersection_update:- It can intersection and update to main variable of set        '''

city1 = {'delhi','noida','bengaluru','mumbai','kochi'}
city2 = {'kolkata','chenai','kochi','mumbai','noida'}
city1.intersection_update(city2)
print(".intersection_update() :- ",city1)



'''       symmetric_difference():- It can remove those available in both set and store in new variable of set.'''


city1 = {'delhi','noida','bengaluru','mumbai','kochi'}
city2 = {'kolkata','chenai','kochi','mumbai','noida'}
city3 = city1.symmetric_difference(city2)
print("symmetric_difference():- ",city3)


'''     '''

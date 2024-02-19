
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print("Isdisjoint :- ",cities.isdisjoint(cities2))


set = {1,2,3,4,5,6,7,8}
set2 = {9,10,11,12,13,14}
print("Isdisjoint :- ",set.isdisjoint(set2))

set3 = {1,2,3,4,5,6}
set4 = {3,4,5}
print("Issuperset :- ",set3.issuperset(set4))


set3 = {1,2,3,4,5,6}
set4 = {3,4,5,7}
print("Issuperset :- ",set3.issuperset(set4))


set5 = {1,2,3,4,5,6}
set6 = {3,4,5}
print("Issubset :- ",set6.issubset(set5))


set5 = {1,2,3,4,5,6}
set6 = {3,4,5}
print("Issubset :- ",set5.issubset(set6))



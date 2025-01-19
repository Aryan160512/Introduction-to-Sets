set1 = {1, 2, True, 3, 4, 'Hello World', 5, 6}
set2 = {0, False, 1, True, 34, 64, 23, 63, 34, 'This element will be removed'}

#Modifying Sets
set1.add('This element is added')
set2.remove('This element will be removed')

#Iterating Through Sets
for element in set1:
    print(element)

#Checking If an Element Exists
if True in set2:
    print('True is in the set')
else:
    print('Element not found')

#Set Operations
set3 = {1, 2, 3, 4, 5}
set4 = {5, 6, 7, 8, 9}

#Union
print(set3.union(set4))
print(set3 | set4)

#Intersection
print(set3.intersection(set4))
print(set3 & set4)

#Difference
print(set3.difference(set4))
print(set3 - set4)

#Symmetric Difference
print(set3.symmetric_difference(set4))
print(set3 ^ set4)
set1 = {44, 54, 55, 44, 34, 12}
set2 = {True, False, 0, 1}

#The set() Constructor
set3 = set([34, 54, 23, 73, 23, True, 'Hello World', 'This element will be removed'])
#NOTE: It is also possible to use the set() constructor to make a set. It converts a list into a set.

set4 = {45, 534, 456, 465, True, 'Hello World', 'This element will be removed'}

#Printing a Set
print(set1)

#print(set1[2]) --- NOTE: Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#Checking for Membership of an element
if 23 in set3:
    print('Yes')
else:
    print('No')

#Binary and Boolean
print(set2)
#NOTE: The values True and 1 are considered the same value in sets, and are treated as duplicates
#NOTE: The values False and 0 are considered the same value in sets, and are treated as duplicates

#Get the Length of a Set
print(len(set1))
#NOTE: To determine how many items a set has, use the len() function.

#Adding New Elements to Sets
set1.add('This is a new element')
print(set1)

#Deleting an element from a set
#Method 1: Using remove function
print(set3)

set3.remove('This element will be removed')
print(set3)

#set3.remove('This element is not in the set')
#print(set3)

#Method 2: Using discard function
print(set4)

set4.discard('This element will be removed')
print(set4)

set4.discard('This element will not cause an error')
print(set4)


#Using Set Operations
set5 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25}
set6 = {0, 5, 10, 15, 20, 25, 30, 35}

#The union operation
print(set5.union(set6))

print(set6 | set5)

#The intersection operation
print(set5.intersection(set6))

print(set6 & set5)

#The difference operation
print(set5.difference(set6))

print(set6 - set5)

#The symmetric difference
print(set5.symmetric_difference(set6))

print(set6 ^ set5)
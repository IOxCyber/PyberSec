# set {values}: Unordered (Can't access by "Index"), unique values & mutable

'''# Example 1:
my_set = {1,2,3,4,4,5,5} # duplicate values will be discarted from set
print(my_set)

my_set.add(100) # add a unique value
my_set.add(5) # will not be added (Duplicated)

print('After adding 100:',my_set)


# Example 2:
# list(duplicate values) to set(unique values)
my_list = [1,2,3,4,4,5,5]
new_set = set(my_list)
set_copy = new_set.copy()

print('New Set:',new_set)
print('Set Copy:',set_copy)

# set to list
my_set1 = range(1,5)
my_list1 = list(my_set1)
print(my_list1)'''


# Set methods:
# Example 3:

set1 = {1,2,3,4,5} 
set2 = {4,5,6,7,8,9,10}

print('Difference: ',set1.difference(set2)) # remove duplicate values & show difference from set1

#print(set1.intersection(set2)) # common values
print(set1 & set2 ) # same as intersection, values in set as well as set2

set1.discard(5) # in place method
print('After Discard 5:',set1)

print(set2)
print(set1.isdisjoint(set2)) # true if both sets have unique values

# print(set1.union(set2)) # merges both sets with unique
print(set1 | set2) # same as union, value either in set1 or set2

print(set1.issubset(set2)) 
print(set1.issuperset(set2)) 
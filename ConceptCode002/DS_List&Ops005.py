# First Data Structure - List (think it as array)
# List slicing [start:end-1:stepover]
# Everytime we do list slicing, a new list will be created

# Example 1: Copy vs Modifing the list
amazon_cart = ['Notebooks', 'Sunglasses', 'Pen', 'Toy', 'Grapes']

amazon_cart[0] = 'Computers'  # modified 1st indexed item

## Why [:] not just amazon_cart in assignment?
new_list = amazon_cart[:]  # try with amazon_cart or use copy() method.
new_list[0] = 'gum'

# Avoid assigning the one list to another because in python both list will point to same memory.
# then if we'll modify one list, it will affect the other list as well.
# To avoid this we can use [:] slicing method or in-built list copy() when assign one list to another.

print(new_list)
print(amazon_cart)

# Example 2:

li1 = [1, 2, 3, 4, 5]
li2 = li1  # both lists now points to same address.
li2[0] = 23  # this modification will affect li1 too.
print(id(li1), id(li2))
print(li2, li1)

# Matrix: array within array or list within list

matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

print(id(matrix))  # address
print(id(matrix[0]))  # address of 0th Indeex item

print(matrix)  # print matrix
print(matrix[0][0])  # 0th indexed list's 1st element.
print(matrix[0:2])  # list slice

## List in-place methods (No value return, modify in memory coz immutable Data type: list) ##

# these methods are in-place methods.
# in-place modification means change the value in a memory region & doesn't create new list or RETURN a value.

basket = [1, 2, 3, 4, 5]
new_list0 = basket.append(
  122
)  # will output as "None" coz append() in-place method doesn't return a value.
print(new_list0)

# append()
basket.append(122)  # added at last of list
print(basket)

new_list = basket[:]
new_list[0] = 100
print(new_list)

# extend()
basket.extend([9, 9.9, 99, 999])
print(basket)

# insert()
basket.insert(0, 99)  # insert value at specific index
print(basket)

# removing items
basket.remove(9.9)  # remove specific value/item
print(basket)

# Non-in place method, means returns a value
print('Removed: ', basket.pop(6))  # remove specific value/item by index
basket.pop()  #from last
print(basket)

# clear()
new_list.clear()  # returns --> None
print('All items removed.', new_list)

# More methods
basket2 = ['d', 'b', 'e', 'a', 'c', 'f']

# get index of item
print(basket2.index('c'))

print(basket2.index('c', 0, 5))  # get index of c in a range 0-5

# using "in" keyword search in list
print('c' in basket2)

# sorted (non-in place method)
new_lists = sorted(basket2)
print('sorted:', new_lists)  # new list created
print(basket2)  # unmodified by sorted

# sorting (in place method)
basket2.sort()
print('sort():', basket2)

# reverse() - in place methods
basket2.reverse()
print('Reverse:', basket2)

# First Data Structure - List (think it as array)
# List slicing [start:end-1:stepover]
# Everytime we do list slicing, a new list will be created.


amazon_cart = ['Notebooks', 'Sunglasses', 'Pen', 'Toy',
               'Grapes']


amazon_cart[0] = 'Computers' # modified 1st indexed item

## Copy vs Modifing the list
## Why [:] not just amazon_cart in assignment? 
new_list = amazon_cart[:] # try with amazon_cart
new_list[0] = 'gum'

# Avoid assigning the one list to another because in python both list will point to same memory.
# then if we'll perform an operation on one list, will affect the other list as well.
# To avoid this we can use [:] slicing method when assign one list to another.

print(new_list)
print(amazon_cart)
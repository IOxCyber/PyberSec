# Tuple (think as immutable list): Ordered, unchangeable
# no modification, no update allowed in tuple unlike list.
my_tup = (1,2,3,4,4,5,6,7,7)

# tuple slicing
new_tup = my_tup[0:5] 

print('my_tuple:',my_tup)
print('new_tuple:',new_tup)

# unpacking
x,y,*z = new_tup
print(x,y,z)

# my_tup[0] = 1 # not possible
print(my_tup[0]) # access an item
print(1 in my_tup) #search for a item

# count() the value
print('Count of Number 4 is: ',new_tup.count(4))

# Index() of a number
print('Index of Number 4 is: ',new_tup.index(4))

# Length
print('Length of new_tuple is: ',len(new_tup))



# Example 2: tuple as key.

dict2 = {
  'An_String' : 'Yes_Possible',
  123 : 1,
  True : False,
  'Key must be Immuatable' : 'must not change',
  (1,2) : [1,2,3] # using tuple
  # lst : 'not possible' # Dict keys must be immutable type i.e unchangeable
}

print(dict2[(1,2)])
print(dict2.popitem())


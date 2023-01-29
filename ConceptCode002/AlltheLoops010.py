# for loops: to repeat a specific block of code a known number of times.

# Iterables: An Object/collection of items that can be iterable over. eg. list, dict, set, tuple, strings.

# for item in Iterable.
print("Strings")
for item in "String is cool":
  print(item)

print("Lists")
for num in [1, 2, 3, 4, 5]:
  print(num)

print("Tuples")
for num2 in (1, 2, 3, 4, 5):
  print(num2)

print("Sets")
for items2 in {2, 3, 4, 5, 5, 6, 6}:  # no duplicate value
  print(items2)

print("Dictionary")
dicts = {
    'key1': 40,
    'key2': 45,
    'key3': 50,
    'key4': 50
}  # no duplicate value

for items in dicts: # without in-built method -> prints keys
  print(items)

for items in dicts.keys(): # prints keys.
  print(items)

for items in dicts.values(): # prints values.
  print(items)

for items in dicts.items(): # .items() -> prints both as tuple
  print(items)

for k,v in dicts.items(): # we can use key,value for looping in dict.
  print(k,v)
  
# nesting of loops:
for x in (1, 2, 3, 4, 5):  # tuple
  for y in ['a', 'b', 'c']:  # list
    print(x, y)

# range(start,end,stepover) function: to make iterable via a number.

for x in range(0, 10, 2): 
  print(x)


for _ in range(0, 10, 2): # can we used when no need for var name.
  print(_)

for _ in range(10, 0, -1): # decending
  print(_)

for _ in range(2):
  print(list(range(5)))


# enumerate(): takes a collection (e.g. list, tuple, string, dict) and returns it as an enumerate object. 
# adds a counter as the key of the enumerate object.

print("String")
for index, char in enumerate('String'):
  print(index, char)

print("Tuple")
for index, char in enumerate((1,2,3,4,5)):
  print(index, char)

print("List")
for index, char in enumerate([1,2,3,4]):
  print(index, char)

# Exercise: index of a number
for index, char in enumerate(list(range(100))):
  if char == 50:
    print(f'index of 50 is: {index}')



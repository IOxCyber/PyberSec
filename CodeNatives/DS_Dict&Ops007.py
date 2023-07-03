# Dictionary: (Hash table, Map in other language)
# var = { key:value }
# Dict are unordered DS means the items are not store in memory in sequence hence can't access by "index" like list. 

print('\n Example 1: Dictionary \n')
dict1 = {
  'a' : [1,2,3],
  'b' : 'Hello',
  'c' : False,
  'c' : True # Overwrite key 'c' value
  }

print(dict1)
print(dict1['b']) # access items
print(dict1['a'][0]) # 1




print('\n Example 2: hetrogenous dict \n')

dict2 = {
  'An_String' : 'Yes_Possible',
  123 : 1,
  True : False,
  'Key must be Immuatable' : 'must not change'
  (1,2) : [1,2,3]
  # lst : 'not possible' # Dict keys must be immutable type i.e unchangeable
}

print(dict2)

# print(dict1[0]) # error, dict can't be accessed by "index"
# duplicate key will be overwrite with latest value, Key has to be unique.




print('\nExample 3: get(\'key\',default_value)\n')

user1 = {
  'basket' : [1,2,3],
  'greet' : 'hello',
  'name' : 'Jojo'
}

print(user1.get('age', 27)) 
print(user1.pop('name')) # remove by keys
print(user1.update({'age': 27})) # update a key, value
print('User1:',user1)

# using built-in function: dict(key='value')
user2 = dict(name='Sunny')
print(user2)

print('name' in user1)
print('age' in user1.keys())
print('Jojo' in user1.values())
print(user1.items()) 
# user1.clear() # removed dict
print('Second Dict:',user2)

### String ###

# 012345 (Index)
# -5-4-3-2-1 (-ve Index)

var1='String is Awesome'

# Strings store as list in Memory in Python means can be accessible by index.
print(var1) # String is Awesome
print(var1[0],var1[10]) # S A

### String Slicing var[start:end-1:stepover] ###

# var1[start:end-1]
print(var1[0:6]) # String

# var1[start:end-1:stepover]
print(var1[0::2]) # Skip one value

# var1[start:end-1:Negative Stepover]
print(var1[::-1]) # emosewA si gnirtS


### Formatted String ###
''' 
- the process of inserting a custom string or variable in predefined text.
- 2 ways i.e using print(f"string with {variable}") & string.format(var="value")
- placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}'''

# Example f"string
name = "Steve"
greet = "Perfect!"
print(f'Hi {name}, you are {greet}')

# Example string.format(var="value")
print('Hi {}, you are {}'.format('Steaverr', 'Great'))  # empty placeholders {}

print('Hi {username}, you are {greeting}'.format(username='Stuard', greeting='Perfect'))  # Named placeholders {}

print('Hi {0}, you are {1}'.format('Ferrv', 'Awesome'))  # numbered indexes {0} 


### String Immutablity ###
str = 'A B C D E'
print(str)

# String modified here & new temp new str var created & destroyed after execution comleted but Original string never chages as "String" is immutable
print(str.replace('A', 'Z'))
print('')
print(str)

### booleans ###
# bool i.e True (1) or False (0)
var1 = False
var2 = True

# integer to boolean
print(bool(0)) 



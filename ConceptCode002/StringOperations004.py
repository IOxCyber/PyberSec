# String Slicing

# 012345 (Index)
# -5-4-3-2-1 (-ve Index)

var1='String is Awesome'

# Strings store as list in Memory in Python means can be accessible by index.
print(var1) # String is Awesome
print(var1[0],var1[10]) # S A

# String Slicing
# var1[start:end-1]
print(var1[0:6]) # String

# var1[start:end-1:stepover]
print(var1[0::2]) # Skip one value

# var1[start:end-1:Negative Stepover]
print(var1[::-1]) # emosewA si gnirtS


'''Formatted String: 
1. the process of inserting a custom string or variable in predefined text.
# 2 ways i.e using print(f"string with {variable}") & string.format(var="value")
# placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.'''

# Example
name = "Steve"
greet = "Perfect!"
print(f'Hi {name}, you are {greet}')
print('Hi {}, you are {}'.format('Steaverr', 'Great'))  # empty placeholders {}
print('Hi {0}, you are {1}'.format('Ferrv', 'Awesome'))  # numbered indexes {0} 
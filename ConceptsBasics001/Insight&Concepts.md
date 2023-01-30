## :: Insight & Concepts in Python ::

### Datatypes: Fundamental Data Types

- Numberic:
  int (whole numbers as 1234, -10), float(0.0,3.14,-9.01), complex (Not useful for common tasks)
- String: str ("A String")
- Boolean type: bool.
- Sequence types: list, tuple, range.
- Set data types: set, frozenset
- Mapping data type: dict.
- Binary types: bytes, bytearray, memoryview.


### Specialized Data Types: Packages & Modules to add functionality.

### None:  Absence of Value!

### Operator Precedence:
- The order in which an expression is evaluated.
- Parentheses > Exponent > Unary (Plus, Minus) bitwise Not > Multi, Div, Floor, Modulo > Add & Sub > Bitwise shift Opr > Bitwise AND > XOR > OR > Comparisons, Identity, Membership operators > Logical NOT > AND > OR
  

### Associativity: 
- the order in which an expression is evaluated if it has multiple operators of the same precedence.
- Almost all the operators have **left-to-right associativity** means left one is evaluated first.
   

### Augmented assignment Operator:
> short hand for var = var + 1
> var = 1 # defined var
> var -= 1 # use the assignment Operator
> var += 1 # use the assignment Operator


### Immutable Datatypes:
>
> If we do **any operation/modification on immutable datatype**, at run time the **temp variable of that datatype will be created & show the output and get destroyed** as soon as the program terminated.
>

- Int, Float, Tuple, bool, Complex, String, Stringfrozen set [note: immutable version of the set], Bytes
- Can't change internal state of the object i.e memory address & can be checked by id(var)
- as the value changes, the internal state ie memory address (identity) will change.
- immutable objects, you seal the values and ensure that no threads can invoke overwrite/update to your data
- Concept of Immutablity means Address will not modify.
'''


## Example Not-Mutable:
```
var1 = 200  # initialize the variable
print('Variable {1}: Location {0}'.format(id(var1),var1))  # Keep an eye on "memory address in hexadecimal format" 

var1 = 300  # re-assigned the variable
print('Variable {1}: Location {0}'.format(id(var1),var1))   # Keep an eye on "memory address in hexadecimal format" (Changed)
```

## Example Mutable:
```
var2 = ['a','b']
print(id(var2),var2) # Keep an eye on "memory address in hexadecimal format"

var2[1] = 'c'
print(id(var2),var2) # Keep an eye on "memory address in hexadecimal format" (Never Changes)


'''we were able to change the internal state of the object ‘cities’ by adding one more city ‘Chennai’ to it, yet, the memory address of the object did not change. This confirms that we did not create a new object, rather, the same object was changed or mutated.
'''
```

### Address is the type of `int` hence below operations are possible.
```
x = 3
y = 3
print(id(x + y + 6), id(x), id(y - 1))  # all possible

z = id(x) + 1
print(type(id(z)))
```

### In-place list modification [more](https://github.com/cyberqurious/PyberSec/blob/main/ConceptCode002/DS_List&Ops005.py)
- In place (will not return a value, no new list will be created)
- means in-place methods changes the value in a memory region.
- list are mutable, hence new list will not created but modified the original one.

### The non in-place methods of lists returns a value

### Assigning lists `[:] or copy()` [more](https://github.com/cyberqurious/PyberSec/blob/main/ConceptCode002/DS_List&Ops005.py):
- Avoid assigning the one list to another because in python both list will point to same memory.
- then if we'll modify one list, it will affect the other list as well.
- To avoid this we can use [:] slicing method or in-built list copy() when assign one list to another.

### List Unpacking: `(a, b, c) = List/tuple`
- iterable unpacking operator (*), we can unpack muliple values in one variable.
- List Unpacking: list or tuple assigned to a single variable (using *).
- you can use only one unpacking operator (*)

  
### List packing: `def mySum(*args)`
-  wraps all the arguments into a single variable
-  both packing/unpacking possible with list, string, range, set, tuple, dictionary

### Unpacking/packing Example:
```
my_tup = (1, 2, 3)  
print((0, *my_tup, 4))  

my_list = [1, 2, 3]  
print([0, *my_list, 4])  

my_set = {1, 2, 3}  
print({0, *my_set, 4})  

print([*my_set, *my_list, *my_tup, *range(1, 4)])  

my_str = "123"  
print([*my_set, *my_list, *my_tup, *range(1, 4), *my_str])
```
### Ordered & Unordered DS:




### Truthy & Falsy:
- A "truthy" value will satisfy the check performed by if or while statements.

- But **an Empty DS containing other Empty DS will return True** i.e `print(bool([()]))`
`print(bool({''}))`

- All values are considered "truthy" except for the following, which are all "falsy":
```
None
False
Numbers that are numerically equal to zero, including:
0
0.0
0j
decimal.Decimal(0)
fraction.Fraction(0, 1)
Empty sequences and collections, including:
[] - an empty list
{} - an empty dict
() - an empty tuple
set() - an empty set
'' - an empty str
b'' - an empty bytes
bytearray(b'') - an empty bytearray
memoryview(b'') - an empty memoryview
an empty range, like range(0)
objects for which
obj.__bool__() returns False
obj.__len__() returns 0, given that obj.__bool__ is undefined
```


### Short Circuiting: [more](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- the stoppage of execution of boolean operation if the truth value of expression has been determined already.
```
# Example 1:
expr1 = True
expr2 = True

if expr1 or expr2:  # since expr1 is true, interpreter will never eveluate the expr2
  print('Only first expr is True or 2nd is true')
else:
  print('will only eveluated when both expr are False.')

# Example 2:
expr3 = False
expr4 = True

if expr3 and expr4:  # 'Since expr3 is false, expr4 will never evaluated'
  print('Only when both Expr are True')
else:
  print("Any one condition is False or 1st one is false.")
```



### Ternary Operator/ conditional expression:

```
# condition_if_true if condition else condition_if_else

friends = True

print('Let\'s chat') if friends else print("Blocked.")
```


### ASCII: American Standard Code for Information Interchange, for every character there is a ascii value which converts into binary in order to communicate to Computer.
```
print('a' > 'A') # will compare the ascii value of both letters i.e 97 > 65

N = 97; 
print(chr(N)) # print char against value
print(oct(N))
print((hex(N)))
```

### is vs ==
```
# == The Equality operator (==) compares the values of both the operands and checks for value equality.
print(True == 1)
print('1' == 1)
print([] == 1)
print(10 == 10.0)
print([1,2,3] == [1,2,3])
print('a' == 'a')

# is: For reference equality/ identity Operator, checks the location in memory same or not or belongs to same object
print(True is True)
print([1,2,3] is [1,2,3]) # both list are at different location.
```







[^1]:Bytecode is computer object code that an interpreter converts into binary machine code so it can be read by a computer's hardware processor. The interpreter is typically implemented as a virtual machine (VM) that translates the bytecode for the target platform.

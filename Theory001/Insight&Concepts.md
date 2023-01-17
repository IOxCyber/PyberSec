# : Insight & Concepts in Python :

## Datatypes: Fundamental Data Types

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
- 

### Associativity: 
- the order in which an expression is evaluated if it has multiple operators of the same precedence.
- Almost all the operators have **left-to-right associativity** means left one is evaluated first.
- 

 

### Augmented assignment Operator:
> short hand for var = var + 1
> var = 1 # defined var
> var -= 1 # use the assignment Operator
> var += 1 # use the assignment Operator


### Immutable Datatypes:
>
> **If we do any operation/modification on immutable datatype, at run time the temp variable of that datatype will be created & show the output and get destroyed as soon as the program terminated.**
>

'''
- Int, Float, Tuple, Complex, String, Stringfrozen set [note: immutable version of the set], Bytes
- Changes internal state of the object i.e memory address & can be checked by id(var)
- as the value changes, the internal state ie memory address (identity) will change.
- immutable objects, you seal the values and ensure that no threads can invoke overwrite/update to your data
- Concept of Immutablity means Address will not modify.
'''
```
# Example Not-Mutable:
var1 = 200  # initialize the variable
print('Variable {1}: Location {0}'.format(id(var1),var1))  # Keep an eye on "memory address in hexadecimal format" 

var1 = 300  # re-assigned the variable
print('Variable {1}: Location {0}'.format(id(var1),var1))   # Keep an eye on "memory address in hexadecimal format" (Changed)


# Example Mutable:
var2 = ['a','b']
print(id(var2),var2) # Keep an eye on "memory address in hexadecimal format"

var2[1] = 'c'
print(id(var2),var2) # Keep an eye on "memory address in hexadecimal format" (Never Changes)

'''
we were able to change the internal state of the object ‘cities’ by adding one more city ‘Chennai’ to it, yet, the memory address of the object did not change. This confirms that we did not create a new object, rather, the same object was changed or mutated.
'''
```









[^1]:Bytecode is computer object code that an interpreter converts into binary machine code so it can be read by a computer's hardware processor. The interpreter is typically implemented as a virtual machine (VM) that translates the bytecode for the target platform.

# Data types:
'''
Numeric data types: int, float, complex

String data types: str

Sequence types: list, tuple, range

Binary types: bytes, bytearray, memoryview

Mapping data type: dict

Boolean type: bool (True 1, False 0)

Set data types: set, frozenset
'''

# int & float
print(type(6))
print(5 + 4, (5 - 4))  # Add&Sub
print(6 * 8)  # Multiply
print(6 / 2)
# Division -> Gives Quotient as in (Dividend ÷ Divisor = Quotient + Remainder)

print(2**3)  # Power
print(6 // 2)  # (Quotient) Round Off to closed Integer
print(6 % 2)  # Modulo (Remainder)

# math functions (Search on google for more)
print(round(2.6))
print(abs(2.6))  # No -ve number

# Operater Precedence
print((2+2)*2-4) # () > ** > *, / > +,-

# bin(): To convert the decimal to bin.
print(bin(5))
print(int('0b101', 2))

# string str()
str1 = "with Double Quotes"
str2 = 'with Single Quotes'
str3 = str1
str3 += str1 # concate
print(str3)

# long String
long_str = '''
It's a multi lines string 
 /\
0  0
 --
'''

print(long_str)


# booleans
# bool i.e True (1) or False (0)
var1 = False
var2 = True

# integer to boolean
print(bool(0)) 
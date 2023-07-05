# Example 1: def func( *args )
# List packing: wraps all the arguments into a single variable
def mySum(*args):
  return sum(args)
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))


# Example 2: (a, b, c) = List/tuple
# List Unpacking: list or tuple assigned to a single variable (using *).
# you can use only one unpacking operator (*)

def fun(a, b, c, d):
  print(a, b, c, d)

a, *other = [1, 2, 3, 4]
fun(a, *other)


# Example 3: Dropping Unnecessary Values With *
a, b, *_ = 6, 8, 0, 0, 0, 0  
print(a)  
print(b)  


# Example 4: Power Program
def power(x):
  return x, x**2,x**3

Num,Square,Cube=power(2) # Unpacking returned values to multiple variables

print(Num,Square,Cube)

*_,Cube=power(3)
print(Cube)



# Example 5: Unpacking tuple, list, set, string, range:
my_tup = (1, 2, 3)  
print((0, *my_tup, 4))  

my_list = [1, 2, 3]  
print([0, *my_list, 4])  

my_set = {1, 2, 3}  
print({0, *my_set, 4})  

print([*my_set, *my_list, *my_tup, *range(1, 4)])  

my_str = "123"  
print([*my_set, *my_list, *my_tup, *range(1, 4), *my_str])

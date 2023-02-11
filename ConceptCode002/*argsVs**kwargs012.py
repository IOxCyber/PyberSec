# Example 1:
# *arg vs **kwargs

# *arg: used to pass multiple numbers of arguments to a function.
def super_func1(*args):  # accept any number of args
  return sum(args)

print(super_func1(1, 2, 3, 4, 5))


# **kwargs: accept keyworded variable-length argument passed by the function call in Dictionary datatype
def super_func2(*args, **kwargs):
  # print(kwargs) # a dictionary
  total = 0
  for items in kwargs.values():  # loop over on dict's value
    total += items
  return sum(args) + total

print(super_func2(1, 2, 3, 4, 5, num1=7, num2=8))


# Rule: to define a function the order is as this >> params, *args, default params, **kwargs
# Example 2:
def func(*args, **kwargs):
  a, b, *other = args
  x1, y1 = kwargs
  # print(kwargs)
  return (a + b, other, kwargs.items())


print(func(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, x=23, y=45))

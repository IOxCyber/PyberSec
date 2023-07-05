# In-Built Functions

1. `type(): Returns the type of an object`
```
data_type = type(42)
print(data_type)  # Output: <class 'int'>
```

2. `id()` returns an object’s integer identifier, can be used to check **Object Identity** or a unique identification `value of the object stored in the memory`

3. `dir()`: Returns a list of methods of an object.
```
numbers = [1, 2, 3]
print(dir(numbers))  # It'll return the methods whatever is applicable to the numbers object.
```

4. enumerate(): `yields both the index and value` of each item in an iterable.
```
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

```

5. Return an iterator:
a. `filter(): Filters out elements from an iterable based on a specified condition` and returns an iterator with the filtered results.
```
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]
```

b. `Map(): Applies a function to each item in an iterable` and returns an iterator with the results.
- Syntex: map(function, iterable[, iterable1, iterable2,..., iterableN])
- The argument function can be any Python callable that includes built-in functions, classes, methods, lambda functions, and user-defined functions.
```
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
```

c. `zip(): Returns an iterator that aggregates elements from multiple iterables into tuples.`
```
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
zipped = zip(numbers, letters)
print(list(zipped))  # Output: [(1, 'A'), (2, 'B'), (3, 'C')]
```

6. `isinstance(): Checks if an object is an instance of a specified class` or any of its subclasses.
```
x = 42
print(isinstance(x, int))  # Output: True
```

7. `eval(): Evaluates a string as a Python expression` and returns the result.
```
expression = "3 + 5 * 2"
result = eval(expression)
print(result)  # Output: 13
```

8. Debugging Functions:
a. `callable(): Checks if an object is callable (can be called as a function).`
```
def say_hello():
    print("Hello!")

print(callable(say_hello))  # Output: True

x = 42
print(callable(x))  # Output: False
```

b. `any() and all(): Returns True if any or all elements in an iterable evaluate to True`.
```
numbers = [1, 2, 3, 4, 5]
print(any(numbers))  # Output: True
print(all(numbers))  # Output: True

empty_list = []
print(any(empty_list))  # Output: False
print(all(empty_list))  # Output: True (since there are no elements to evaluate)
```

9. chr() and ord(): `Convert between characters and their corresponding Unicode code` points.
```
print(chr(65))  # Output: 'A'
print(ord('A'))  # Output: 65
```

10. `print(end='\n')`: The end key of print function will set the string that needs to be appended when printing is done. By default the end key is set by newline character.
eg. `set end=''`, mostly used in pattern printing.

11. `range(): Generates a sequence of numbers within a specified range.`
```
eg 1.
numbers = list(range(1, 6))
print(numbers)  # Output: [1, 2, 3, 4, 5]

eg 2.
numbers = list(range(1, 10, 2))
print(numbers)  # Output: [1, 3, 5, 7, 9]
```

12. `help():  to open manual for a function or module.`
> help(list)  # Shows the documentation for the list type
> print(test.__doc__): to open doc string for a function.

13. Conversion Functions:

a. `list(Datatype): converting other collections into lists.`

b. `dict(key='value'): to create dictionary.`
```
user2 = dict(name='Sunny')
print(user2)
```

c. `int(): convert a float to an integer.`
   `float(): convert an integer to a float.`


14. List Operation Functions:

a. `len(): Returns the number of items in an iterable (e.g., string, list, tuple)`
```
length = len([1, 2, 3, 4, 5])
print(length)  # Output: 5
```

b. `sorted(): Returns a new sorted list from an iterable.`
```
unsorted = [3, 1, 4, 2, 5]
sorted_list = sorted(unsorted)
print(sorted_list)  # Output: [1, 2, 3, 4, 5]
```

15. Numbers Operation Functions:
a. `sum(): Calculates the sum of all items in an iterable.`
```
total = sum([1, 2, 3, 4, 5])
print(total)  # Output: 15
```

b. `max() and min(): Returns the maximum and minimum values from a collection.`
```
maximum = max([5, 2, 9, 1])
minimum = min([5, 2, 9, 1])
print(maximum)  # Output: 9
print(minimum)  # Output: 1
```

c. `abs(): Returns the absolute value of a number.`
```
absolute_value = abs(-10)
print(absolute_value)  # Output: 10
```


16. `hex(), bin(), oct(): Converts an integer to hexadecimal, binary, and octal`
```
eg.
print(hex(255))  # Output: '0xff'
print(bin(255))  # Output: '0b11111111'
print(oct(255))  # Output: '0o377'
print(int('0b101', 2)) # convert binary number into integer.
```

16. 


17. To find the largest item in an iterable
- max(iterable, *iterables, key, default)
- to find the largest item between two or more objects
- max(arg1, arg2, *args, key)
- in case of string, max returns the alphabetically largest letter string.








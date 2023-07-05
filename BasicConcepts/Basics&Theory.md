## Basics 101

### Concepts:
1. Python is a dynamic and strongly typed object-oriented programming language.
2. Strong typing means that the type of a value doesn't change in unexpected ways. A string containing only digits doesn't magically become a number, as may happen in Perl, JS(Loosely typed). Every change of type requires an explicit conversion.
3. Dynamic typing means that runtime objects (values) have a type, unlike static typing where variables have a type.
4. The `combination of values, variables, operators, and function calls is termed as an EXPRESSION`.
5. `pass keyword used to simply used as a placeholder for future code`, no error on execution.
6. Documentation Strings: print(my_function.__doc__) to see the comments/documentation("""Any Documenation""") of a program.


### Object:
- Virtually every item of data in a Python is `an object of a specific type or class.`
- eg. check the class of the object as `type(Obj)`. [More](https://realpython.com/python-variables/#object-references)

- Objects are Python’s abstraction for data & is an instance of a Class.
- `Every object has an identity, a type and a value`
- `Identity = address of that the object eg. id(var)
- `Type = Kind of object eg. type(var)
- `Value = Actual value stored in the object eg. print(var)

## Variable & Object:
- A Python `variable is a symbolic name` that is a `reference or pointer` to an object in the memory. Once an object is assigned to a variable, you can refer to the object by that name.

## Function:
- `Piece of code to perform a specific task`
- Functions `explicitly` return a value or object via the `return` keyword otherwise returns `None`.
- `Default Argument` Values must be `declare after Non-Default Argument` in Functions.
> Pass the default value after the Non-default arguments & use return statement to return value from a function.

## Method:
- A method in python is somewhat similar to a function, except it is associated with object/classes.

> None (absance of value) like Null in other language.

## Iterables & Iterator: 
1. Iterable:
- any `object capable of returning its elements one at a time` eg. `list, dict, set, tuple, strings.`
- objects that can be looped over using a for loop.

2. Iterator 
- an object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets.
- iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__() .

# Tips to Learn:
First cover (Terms > Datatypes > Actions > Best Practice)



# Best Practice
1. [CodingDojo](https://www.codingdojo.com/blog/python-best-practices)
2. [Medium](https://medium.com/pythonland/30-python-best-practices-tips-and-tricks-19172564f9c)


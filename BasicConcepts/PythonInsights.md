### 1. ASCII: American Standard Code for Information Interchange, for every character there is a ascii value which converts into binary in order to communicate to Computer.
```
print('a' > 'A') # will compare the ascii value of both letters i.e 97 > 65

N = 97; 
print(chr(N)) # print char against value
print(oct(N))
print((hex(N)))
```

### 2. is vs ==
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


### 3. function vs Method:
- function: can be called independenly. eg. list()
- Rule: to define a function the order is as this >> params, *args, default params, **kwargs


### 4. *args vs **kwargs:
- *arg: used to pass multiple numbers of arguments to a function.
- **kwargs: accept keyworded variable-length argument passed by the function call in Dictionary datatype


### 5. Packages & Modules
- Packages: simply a **folder containing one or more modules**.
- Modules: A set of python **files containing one or more methods** of other package's modules.
- import by `import` keyword or a specific Method of the modules by `from` keyword.
- eg. **import package.module** > use the methods as `package.module.method`
- eg. **from package.module import method** > use the methods as `method`
- eg. **from package import modules** > use the methods as `modules.methods` -- useful to resolve the name collision.


### 6. try-except-finally: [more](https://docs.python.org/3/library/exceptions.html)
```
 try:
    # Error Prone Code
  except ErrorName:
    # Handling Code
  finally:
    # run everytime whether the Error occured or not.
```

### 7. key argument in In-Built Methods:
https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
https://www.w3schools.com/python/python_lambda.asp

### 8. lambda Function: an anonymous function
- 
`def func(p):
   return p.totalScore   
`

### 9. Format Specifier: C-style string formatting to create new, formatted strings
```
var = 4.56745    #Initialising the variable "x"
# using the format specifier "%" to print value till 2 decimal places
print("%.2f" % var)
```

### 10. List Comprehension:







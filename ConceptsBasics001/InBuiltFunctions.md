# In-Built Functions

1. To check the datatype of a var: **type(var)**

2. The combination of values, variables, operators, and function calls is termed as an **EXPRESSION**.

3. **id()** returns an object’s integer identifier, can be used to check **Object Identity** or **a unique identification value of the object stored in the memory**

4. **is** operator used to check the Object Identity. eg: A is B.

5. **pass** keyword used to simply used as a **placeholder for future code**, no error on execution.

6. Documentation Strings: print(my_function.__doc__) to see the comments/documentation("""Any Documenation""") for a program.

7. **int()**: convert a float to an integer.
   **float()**: convert an integer to a float.

8. **bin()**- use to convert integer into the Binary.
```eg.
print(bin(5)) #convert the 5 into binary number '0b101'
print(int('0b101', 2)) # convert binary number into integer.
```

9. **len(string)**: Use to calculate the length of string.

10. **list(Datatype)** constructor is very handy for converting other collections into nice and simple lists.

11. **dict(key='value')**: to create dictionary.
```
user2 = dict(name='Sunny')
print(user2)
```

12. **ord('A')**: To get the Unicode value of a char. 

13. **range()** function: to make iterable via a number.

14. **print(end='\n')**: The end key of print function will set the string that needs to be appended when printing is done. By default the end key is set by newline character.
eg. `set end=''`, mostly used in pattern printing.

15. **help():**  to open manual for a function.

> print(test.__doc__): to open doc string for a function.

16. To find the largest item in an iterable
- max(iterable, *iterables, key, default)
- to find the largest item between two or more objects
- max(arg1, arg2, *args, key)
- in case of string, max returns the alphabetically largest letter string.

17. 

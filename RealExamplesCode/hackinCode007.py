# To use the lowercase alphabets
import string 
x=string.ascii_lowercase
print(x)

# To print longest string of a list:
# Use inbuilt method max(iterable, key=len)
# Example
def longest_word(text):
    try:
        ls = list(text.split())
        result = max(ls, key=len)
        return result
    except ValueError:
        pass
longest_word("Python is pure OOPs language.")


# 
# Example: sorting [https://docs.python.org/3/howto/sorting.html]
# list.sort() - in-place sorting/returns None VS sorted(list) - returns a sorted list

# Write a function named sort_by_mark that take as argument a list of students and returns a copy of it sorted by mark in descending order
def sort_by_mark(my_class):
  ls = sorted(my_class)
  return ls[::-1]
      
# Write a function named sort_by_name that take as argument a list of students and returns a copy of it sorted by name in ascending order
def sort_by_name(my_class):
  ls = sorted(my_class, key=lambda my_class: my_class[1])     
  return ls



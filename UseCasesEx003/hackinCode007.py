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


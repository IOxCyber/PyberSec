# Code

'''
def is_even(num):
  if (num % 2 == 0):
    return True
  elif (num % 2 == 1):
    return False
'''


# Cleaner Code
def is_even(num):
  return (num % 2 == 0) # evaluate as True/False
    

# Function calling
print(is_even(50))
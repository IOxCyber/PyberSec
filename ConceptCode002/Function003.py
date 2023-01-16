# Function definition with "number of parameters" & Default Argument Values.
# Remember to pass the default value after the Non-default arguments
def add_two_numbers(number_one, number_two=5):
  return number_one + number_two  # Returns the sum of the numbers, and is indented by 2 spaces.


# Defining 2nd function
def stringConcate(string_one, string_two):
  return string_one + string_two


# Calling function with Function_Name(number of arguments)
print(add_two_numbers(4, 8))  # 12

# with default value
print(add_two_numbers(4))  # 9

# Calling 2nd function
print(stringConcate("Hello", str(77)))

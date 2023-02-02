# Error Handling: try-except-finally
# try: (put error prone code in it)
# except: (put the error handling code)
# finally: No matter what finally statement will execute after every iteration.


# Example 1:
while True:
  try:
    age = int(input("Enter Age: "))
    print(age)
    break
  except:
    print("Try again, Age must be a number.")

# Example 2:
while True:
  try:
    age = int(input("Enter Age: "))
    10 / age  # different type of Error
  except ValueError:  # 1st error handled
    print("Try again, Age must be a number.")
  except ZeroDivisionError:  # 2nd error handled
    print("Try again, Age must be greater than Zero.")
  else:
    print('Thank you!')
    break

# Working of code > while > try > error? > catch it in except > go to while now.


# Example 3:
def sum(n1, n2):
  try:
    return n1 + n2
  except TypeError as err:  # Always try to catch the ErrorName
    # as err > Storing the error message in err
    print(f"Something wrong: {err}")


print(sum(1 + '2'))


# Example 4:
while True:
  try:
    age = int(input("Enter Age: "))
    10 / age  # different type of Error
  except (ValueError, ZeroDivisionError):  # 1st error handled
    print("Try again, Age must be a number & greater than zero.")
  else:
    print('Thank you!')
    break
  finally: # run after every iteration executed.
    print("Logs captured.")
# Example 5:
while True:
  try:
    age = int(input("Enter Age: "))
    10 / age  # (Error Prone Code)
  except ValueError:  # 1st error handled
    print("Try again, Age must be a number.")
    continue
  except ZeroDivisionError:  # 2nd error handled
    print("Try again, Age must be greater than Zero.")
    break
  else:
    print('Thank you!')
  finally:
    print('Finally, run everytime!')
  print('The-End!')

# Working of code > while > try > error? > catch it in except > go to while now.
  
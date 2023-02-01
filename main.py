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
  finally:
    print("Logged captured.")
  print("dff")
import datetime

birth_year = int(
  input("What year you were born?\n"))  # user input & convert to int

current_year = datetime.date.today(
).year  # using datetime module, get the year

age = current_year - birth_year

print(f'your age is {age}')  # using string formatting to print the output.

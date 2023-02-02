# IO Files Operation:

my_file = open('test.txt')  # open 'file' & store in a variable
print(my_file)

print(my_file.read())  # read the file
# print(my_file.read()) # We can read a file only once as Python read files by Cursor & after reading a file, the cursor will be at end of the file.
my_file.seek(0)  # to reset the cursor to start of file.
print(my_file.read())  # to again read the file

# read a line of the file
print(my_file.readline())
my_file.seek(0)

# read all the lines & returns the List of lines:
print(my_file.readlines())

# To close the file:
my_file.close()

# test.txt file is necessary to run below code
# pathlib - object oriented filesystem paths.

# with keyword: will close the file for you at the end of the block:
# Syntex: with open('fileName',Mode='a/r/w') as testFile

# To append a file:
with open('sad.txt', mode='a') as my_file:
  text = my_file.write('):')
  print(text)

# To read a file: from an absolute path
with open('sad.txt', mode='r') as my_file:
  print(my_file.read())

# checking if file exist, if not then raising the error on terminal.
try:
  with open('sadest.txt', mode='r') as my_file:
    print(my_file.read())
except FileNotFoundError as err:
  print('File doesn\'t exist.')
  raise err  # raising the error on terminal.
except IOError as err:
  print('IO error here!')
  raise err  # raising the error on terminal.

# Standard way to read a file:
with open('sad.txt') as my_file:
  print(my_file.readline())

# To read, write, append: mode=r,r+(to write),a (default= r)
with open('tests.txt', mode='a') as my_file:
  text = my_file.write(':)')
  # cursor reset to start of the file & overwrite the text to avoid this use 'a' - append option.
  # 'w' - write a text to file & create a file.
  print(text)
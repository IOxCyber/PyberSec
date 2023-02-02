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
# To append a file:
with open('sad.txt', mode='a') as my_file:
  text = my_file.write('):')
  print(text)

# To read a file: from an absolute path
with open('sad.txt', mode='r') as my_file:
  print(my_file.read())

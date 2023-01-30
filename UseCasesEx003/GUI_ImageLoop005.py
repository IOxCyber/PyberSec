# First GUI: whenever encounter Zero, print "blank Space" & print * on 1.
picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0],
]

# loop over picture
for row in picture:
  for pix in row:
    if (pix == 0):
      print(' ', end='')
    else:
      print('*', end='')
  print('\n')
  

# Modified/Clean Code:

# First GUI: whenever encounter Zero, print "blank Space" & print * on 1.
picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0],
]

# loop over picture
star='^' # useful when we have to change in more location
empty=' '
for row in picture:
  for pix in row:
    if pix: # can also do (pix == 0) but pix is either 0 or 1 so, it'll run as True/False
      print(star, end='') # end to set/unset the newline char in print stmt.
    else:
      print(empty, end='')
  print('')




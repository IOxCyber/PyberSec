# Simple Password checker

user = input('Enter Username\n')
password = input('Enter Password\n')
pass_len = len(password)
hashed_pass = pass_len*'*'

print(f' Hi {user}, your password {hashed_pass} is {pass_len} letters long') # fun fact if you do {True} or {len}, code won't give error.
# Example 1:

# This function will ask user input until the input matches with defined lists or raise error if retries < 0

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


print(ask_ok('OK to overwrite the file?', 2)) # within print

ask_ok('OK to overwrite the file?', 2) # call directly


# Function 2:


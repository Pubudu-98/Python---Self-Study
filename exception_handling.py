#---Exception Handling in Python---
# Exception handling is a way to gracefully handle errors in the code.
# It allows the program to continue running even if an error occurs.
# The try-except block is used to catch exceptions and handle them.

# Handling Exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print('This is a zero division error!')

# Else and Finally blocks
try:
    value_1 = int(input('Enter a number: '))
except ValueError:
    print('You did not enter a valid number!')
else:
    print('Your number is', value_1)
finally:
    print('Execution is completed!!!')
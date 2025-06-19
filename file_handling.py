#---File Handling in Python---
# Python provides built-in functions for file handling, allowing you to read from and write to files.
# Basic file handling operations include:
# - Opening a file  (for reading or writing)
# - Reading from a file
# - Writing to a file
# - Closing a file

# Read a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Write to a file
with open('example.txt', 'w') as file:
    file.write('Hello, This is a test file.')

# Append to a file
with open('example.txt', 'a') as file:
    file.write('Adding a new line to the file.')

# Binary file handling
with open('example.jpg', 'rb') as file:
    image_data = file.read()
# --Dictionaries
# Unordered collections of key-value pairs.
# Keys must be unique and immutable (strings, numbers, or tuples).
# Values can be of any type and can be duplicated.

student = {
    'name' : 'Pubudu Piyumal',
    'age' : '26',
    'subject' : 'CS - Python'
}

print('This is a dictionary: ', student)
print(type(student))

# Accessing values using keys
print(student['name'])
print(student['subject'])

# Adding a new key-value pair
student['university'] = 'University of Wolverhampton'
print(student['university'])

# Removing a key-value pair
del student['subject']
print('After removing subject: ', student)

# Iterating through keys and values
for key, value in student.items():
    print({'key' : key, 'value' : value})
# --List / Tuple / Set in Python

# -Lists
# Lists are mutable, ordered collections of items.
fruits = ['apple', 'banana', 'cherry']
print('This is a list', fruits)
print(fruits[0]) # accessing the first item
fruits.append('orange') # adding an item
print('After append: ', fruits)
fruits.remove('banana') # removing an item
print('After remove: ', fruits)

# -Tuples
# Tuples are immutable, ordered collections of items.
# They cannot be changed after creation.
fruits_tuple = ('apple', 'banana', 'cherry')
print('This is a tuple: ', fruits_tuple)
print(fruits_tuple[0])  # accessing the first item

# -Sets
# Sets are unordered collections of unique items.
# They do not allow duplicate values.
# They are mutable, meaning you can add or remove items.
color = {'red', 'yellow', 'green'}
print('This is a set', color)
color.add('blue')
print('After add the new item', color)
color.add('red') # Adding a duplicate item has no effect in Sets in python.
print('After adding a duplicate item', color)

# Exercise
# --List / Tuple / Set in Python

# -Lists
# Lists are mutable, ordered collections of items.
# They can contain duplicate values and can be modified after creation.
# Lists are defined using square brackets [].
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
# They can contain duplicate values.
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
cars = ['Swift', 'A45S', 'Civic']
print('This is a list: ', cars)
cars.append('Corolla')
print('After appending a new item: ', cars)

cars_tuple = tuple(cars) # Converting a list to a tuple
print('This is a tuple: ', cars_tuple)
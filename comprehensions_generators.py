#---Comprehensions and Generators in Python---
# Comprehensions are compact ways to create sequences (like lists, dictionaries, or sets) in a single line of code.

#--List Comprehensions
# Creates a new list by applying an operation to each item in an existing iterable.
# expression for item in iterable if condition
numbers = [1,2,3,4,5,6,7]
squared = [x**2 for x in numbers if x % 2 == 0]
print(squared)

#--Dictionary Comprehensions
# Create a dictionary by transforming or filtering data.
names = ['Alice', 'Bob', 'Charlie']
lengths = {name: len(name) for name in names}
print(lengths)

#--Set Comprehensions
# Creates a set ensuring unique items.
nums = [1,2,2,3,4,4,5,5,6]
unique_squared = {x**2 for x in nums}
print(unique_squared)

#--Generators
# Generators are iterators that yield items one at a time, allowing memory-efficient processing of large datasets.
def generate_numbers():
    for i in range(1, 10):
        yield i
for num in generate_numbers():
    print(num)
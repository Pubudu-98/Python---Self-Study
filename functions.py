# --Functions in Pythion--
# Functions are defined using the `def` keyword.
# Functions can take parameters and return values.
# Functions can be called by their name followed by parentheses.

def function_name (parameter):
    # function body
    return parameter

def greet(name):
    return print('Hello,', name)

message1 = greet('Pubudu')
print(message1)
message2 = greet('Alice')
print(message2)

# -Exercise
def add(a, b):
    return print (a + b)
result = add(3, 5)
print(result)

#-Exercise to calculate area
def calculate_area(length, width):
    return length * width
area = calculate_area(10, 20)
print('Area of the sqaure: ', area)
    

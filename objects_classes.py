# -- OOP in Python --
# Python is an Object-Oriented Programming language.
# What are Classes and Objects?
# - Class: A blueprint or template for creating objects (defines properties and behaviors).
# - Object: An individual instance of a class (represents a specific entity).

# Basic class definition syntax:
# class ClassName:
#     def __init__(self, parameters):
#         # Constructor to initialize object properties
#         self.property = property_value
#
#     def method_name(self):
#         # Define behaviors (methods)
#         return result
    

# This code demonstrates the creation of a class and its objects in Python.
# --Classes and Objects in Python--
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def details (self):
        print('This is ', self.make, self.model, self.year, ' car.')

# Create objects and call methods
car1 = Car('Toyota', 'Corolla', 1986)
car2 = Car('Suzuki', 'Swift', 2007)

car1.details()
car2.details()
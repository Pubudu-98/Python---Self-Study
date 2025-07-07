#---Modules and Packages in Python---#
# A module is a python file (.py) that contains variables classes functions.
# We can import a module to another python file to reuse the code.

#--Built in Python Modules
# math: Advance math functions
# random: Random number genration
# datetime: Working with dates and time
# os: Operating system tasks

import math
from operator import add
from numpy import subtract

print(add(2,4))
print(subtract(10, 4))

import random
print(random.randint(1,10))

#--Import Variations
# import module: Full import
# from numpy import subtract: Import specific part from a module
# import module_name as alias: Import with alias

from math import pi
print(pi)

import random as rnd
print(rnd.choice([1,2,3]))

#--Python Packages
# A collection of python modules.
# Grouped in a folder
# Useful for structuring large scale projects.
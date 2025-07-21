# Python Self-Study — ShortNote Book

Welcome to the **Python Self-Study** repository!  
This is a concise theory “ShortNote” book for Python fundamentals, organized for quick reference and rapid revision. Each section covers the essentials—definitions, differences, and key examples.

---

## Table of Contents

1. Hello World
2. Basic Operations
3. Collections
4. Conditional Statements & Loops
5. Dictionaries
6. File Handling
7. Functions
8. Object-Oriented Programming (OOP)
9. Comprehensions & Generators
10. Modules & Packages

---

## 1. Hello World

- Output with `print()`:
  ```python
  print("Hello, World!")
  ```
  The most basic Python code. Useful for debugging and interaction.

---

## 2. Basic Operations

- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Assignment: `=`
- Data types: `int`, `float`, `str` (no need for type declaration)
- Example:
  ```python
  a = 10
  b = 5
  print(a / b)
  ```
- User input:
  ```python
  name = input("Your name: ")
  ```

---

## 3. Collections

- **List**: Mutable, ordered
  ```python
  l = [1, 2, 3]
  ```
- **Tuple**: Immutable, ordered
  ```python
  t = (4, 5, 6)
  ```
- **Set**: Mutable, unordered, unique items
  ```python
  s = {1, 2, 2, 3}  # {1, 2, 3}
  ```

---

## 4. Conditional Statements & Loops

- **If/elif/else**:
  ```python
  if n > 5:
      print("Greater than 5")
  elif n == 5:
      print("Equal to 5")
  else:
      print("Less than 5")
  ```
- **Comparison operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical operators**: `and`, `or`, `not`
- **Loops**:
  ```python
  for i in range(3):
      print(i)
  ```
  ```python
  x = 0
  while x < 3:
      print(x)
      x += 1
  ```

---

## 5. Dictionaries

- **Definition**:
  ```python
  d = {"name": "Bob"}
  ```
- **Add/update**:
  ```python
  d["age"] = 25
  ```
- **Looping**:
  ```python
  for k, v in d.items():
      print(k, v)
  ```

---

## 6. File Handling

- **Open/Write**:
  ```python
  with open("test.txt", "w") as f:
      f.write("Hello")
  ```
- **Read**:
  ```python
  with open("test.txt", "r") as f:
      print(f.read())
  ```
- Modes: `'r'` (read), `'w'` (write), `'a'` (append), `'b'` (binary)

---

## 7. Functions

- **Define**:
  ```python
  def square(x):
      return x * x
  ```
- **Parameters with defaults**:
  ```python
  def add(a, b=2):
      return a + b
  ```
- **Docstring**:
  ```python
  def greet():
      """Print a greeting message."""
      print("Hello")
  ```

---

## 8. Object-Oriented Programming (OOP)

- **Class and object**:
  ```python
  class Car:
      def __init__(self, make, model):
          self.make = make
          self.model = model
      def details(self):
          print(self.make, self.model)

  mycar = Car("Toyota", "Corolla")
  mycar.details()
  ```

---

## 9. Comprehensions & Generators

- **List comprehension**:
  ```python
  squares = [x**2 for x in range(5)]
  ```
- **Dictionary comprehension**:
  ```python
  name_lengths = {name: len(name) for name in ["Ann", "Bob"]}
  ```
- **Set comprehension**:
  ```python
  unique = {x % 3 for x in range(10)}
  ```
- **Generator**:
  ```python
  def count_up():
      for i in range(5):
          yield i
  for num in count_up():
      print(num)
  ```

---

## 10. Modules & Packages

- **Module**: Any `.py` file.  
  Example:
  ```python
  import math
  print(math.pi)
  ```
- **Import from module**:
  ```python
  from os import path
  ```
- **Custom module**: Place your own `.py` file in the same directory and import.
  ```python
  import mymodule
  ```
- **Package**: A folder with `__init__.py` and modules inside.
- **Import from package**:
  ```python
  from utils import helper
  helper.some_function()
  ```
- **Aliasing**:
  ```python
  import numpy as np
  ```


Happy Learning! 🚀  
Use this as your quick revision book—read the notes, try the code, and return anytime you need to refresh Python basics or theory for interviews!

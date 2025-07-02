# Python Self-Study — A Theory Book for Python Programming

Welcome to the **Python Self-Study** repository!  
This repository is structured as a "theory book" and practice resource for learning and revisiting Python programming concepts. Each script in this collection is dedicated to a specific core topic in Python, with concise code examples and explanations. Use this as a reference or study guide to reinforce your Python knowledge!

---

## Table of Contents

1. [Hello World](#1-hello-world)
2. [Basic Operations](#2-basic-operations)
3. [Collections (Lists, Tuples, Sets)](#3-collections-lists-tuples-sets)
4. [Conditional Statements & Loops](#4-conditional-statements--loops)
5. [Dictionaries](#5-dictionaries)
6. [File Handling](#6-file-handling)
7. [Functions](#7-functions)
8. [Object-Oriented Programming (OOP)](#8-object-oriented-programming-oop)
9. [How to Use](#how-to-use)
10. [Happy Learning! 🚀](#happy-learning-)

---

## 1. Hello World

- **File:** [`Hello_World.py`](Hello_World.py)
- **Concept:**  
  The simplest Python script. Demonstrates the `print()` function, which outputs text to the console.
- **Example:**
  ```python
  print("Hello, World!")
  ```
- **Key Takeaway:**  
  Every Python program starts with basic output. `print()` is essential for debugging and user interaction.

---

## 2. Basic Operations

- **File:** [`basic_operations.py`](basic_operations.py)
- **Concepts:**  
  - Arithmetic operations: `+`, `-`, `*`, `/`, `//`, `%`, `**`
  - Assigning and using variables
  - Basic data types: `int`, `float`, `str`
  - User input with `input()`
- **Example:**
  ```python
  a = 5
  b = 2
  print(a + b)  # Addition
  print(a ** b) # Exponentiation
  name = input("Enter your name: ")
  ```
- **Key Takeaway:**  
  Python handles numbers and text intuitively. Variables are dynamically typed.

---

## 3. Collections (Lists, Tuples, Sets)

- **File:** [`collections.py`](collections.py)
- **Concepts:**
  - **Lists:** Mutable, ordered collections.  
    - Methods: `append()`, `remove()`, `sort()`
  - **Tuples:** Immutable, ordered collections.
  - **Sets:** Mutable, unordered collections of unique elements.
- **Example:**
  ```python
  my_list = [1, 2, 3]
  my_tuple = (4, 5, 6)
  my_set = {1, 2, 2, 3} # {1, 2, 3}
  ```
- **Key Takeaway:**  
  Choose lists for flexible sequences, tuples for fixed data, and sets for unique items.

---

## 4. Conditional Statements & Loops

- **File:** [`conditional_statements.py`](conditional_statements.py)
- **Concepts:**
  - `if`, `elif`, `else` for decision making
  - Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
  - Logical operators: `and`, `or`, `not`
  - **Loops:** `for` and `while` for repetition
  - Control commands: `break`, `continue`
- **Example:**
  ```python
  age = 18
  if age >= 18:
      print("Adult")
  else:
      print("Minor")

  for i in range(5):
      print(i)
  ```
- **Key Takeaway:**  
  Control flow is fundamental to building logic in any program.

---

## 5. Dictionaries

- **File:** [`dictionaries.py`](dictionaries.py)
- **Concepts:**
  - Key-value data structure
  - Access, add, remove, and update elements
  - Looping through keys, values, and items
- **Example:**
  ```python
  person = {"name": "Alice", "age": 30}
  print(person["name"])
  person["city"] = "NY"
  for key, value in person.items():
      print(key, value)
  ```
- **Key Takeaway:**  
  Dictionaries are ideal for structured, labeled data.

---

## 6. File Handling

- **File:** [`file_handling.py`](file_handling.py)
- **Concepts:**
  - Opening files with `open()`
  - Reading: `.read()`, `.readline()`, `.readlines()`
  - Writing and appending: `'w'`, `'a'` modes
  - Using `with` statement for safe file handling (auto-closes file)
- **Example:**
  ```python
  with open("example.txt", "w") as f:
      f.write("Hello File")

  with open("example.txt", "r") as f:
      content = f.read()
      print(content)
  ```
- **Key Takeaway:**  
  Always use `with` for file operations to prevent resource leaks.

---

## 7. Functions

- **File:** [`functions.py`](functions.py)
- **Concepts:**
  - Defining functions with `def`
  - Parameters and return values
  - Scope (local vs global variables)
  - Docstrings for documentation
- **Example:**
  ```python
  def add(a, b):
      """Return the sum of a and b."""
      return a + b

  result = add(2, 3)
  print(result)
  ```
- **Key Takeaway:**  
  Functions organize code, enable reuse, and clarify intent.

---

## 8. Object-Oriented Programming (OOP)

- **File:** [`objects_classes.py`](objects_classes.py)
- **Concepts:**
  - Classes and objects
  - Constructors: `__init__`
  - Instance attributes and methods
  - Example: Simple `Car` class
- **Example:**
  ```python
  class Car:
      def __init__(self, make, model):
          self.make = make
          self.model = model
      def details(self):
          return f"{self.make} {self.model}"

  my_car = Car("Toyota", "Corolla")
  print(my_car.details())
  ```
- **Key Takeaway:**  
  OOP is used to model real-world entities and relationships in code.

---

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pubudu-98/Python---Self-Study.git
   cd Python---Self-Study
   ```

2. **Run any script:**
   ```bash
   python3 <filename>.py
   ```
   Replace `<filename>` with any of the files listed above.

---

## Happy Learning! 🚀

Use this repository as a living theory book — read the explanations, study the code, and run scripts to experiment. Come back whenever you need to review Python basics or prepare for coding interviews!

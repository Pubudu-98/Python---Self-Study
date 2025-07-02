# Python Self-Study — Theory Book & Practice Scripts

Welcome to the **Python Self-Study** repository!  
This repository is designed as your Python “theory book” and practice reference. Each script explores a core Python concept, combining concise theory with practical code. Use it to learn, revise, or prepare for interviews.

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
9. [Comprehensions & Generators](#9-comprehensions--generators)
10. [How to Use](#how-to-use)
11. [Happy Learning! 🚀](#happy-learning-)

---

## 1. Hello World

- **File:** [`Hello_World.py`](Hello_World.py)
- **Concept:**  
  The classic starting point — demonstrates output with `print()`.
- **Example:**
  ```python
  print("Hello, World!")
  ```
- **Key Point:**  
  `print()` is essential for output and debugging.

---

## 2. Basic Operations

- **File:** [`basic_operations.py`](basic_operations.py)
- **Concepts:**  
  - Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
  - Variables and assignment
  - Data types: `int`, `float`, `str`
  - Getting user input with `input()`
- **Example:**
  ```python
  a = 10
  b = 5
  print(a / b)
  name = input("Your name: ")
  ```
- **Key Point:**  
  Python is dynamically typed and handles basic math and text easily.

---

## 3. Collections (Lists, Tuples, Sets)

- **File:** [`collections.py`](collections.py)
- **Concepts:**
  - **Lists:** Mutable, ordered. Methods like `append`, `remove`, `sort`.
  - **Tuples:** Immutable, ordered.
  - **Sets:** Mutable, unordered, unique items.
- **Example:**
  ```python
  l = [1, 2, 3]
  t = (4, 5, 6)
  s = {1, 2, 2, 3}  # {1, 2, 3}
  ```
- **Key Point:**  
  Lists for changeable sequences. Tuples for fixed collections. Sets for uniqueness.

---

## 4. Conditional Statements & Loops

- **File:** [`conditional_statements.py`](conditional_statements.py)
- **Concepts:**
  - `if`, `elif`, `else` for decision logic
  - Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
  - Logic: `and`, `or`, `not`
  - **Loops:** `for`, `while`; `break` and `continue`
- **Example:**
  ```python
  n = 10
  if n > 5:
      print("Greater than five")
  else:
      print("Five or less")

  for i in range(3):
      print(i)
  ```
- **Key Point:**  
  Control flow is the backbone of program logic.

---

## 5. Dictionaries

- **File:** [`dictionaries.py`](dictionaries.py)
- **Concepts:**
  - Key-value storage
  - Access, add, update, delete items
  - Looping with `.items()`
- **Example:**
  ```python
  d = {"name": "Bob", "age": 25}
  d["city"] = "London"
  for k, v in d.items():
      print(k, v)
  ```
- **Key Point:**  
  Use dictionaries for structured, labeled data.

---

## 6. File Handling

- **File:** [`file_handling.py`](file_handling.py)
- **Concepts:**
  - Open files: `open()`
  - Read: `.read()`, `.readline()`, `.readlines()`
  - Write/append: modes `'w'`, `'a'`
  - Context manager: `with`
- **Example:**
  ```python
  with open("test.txt", "w") as f:
      f.write("Hello file!")

  with open("test.txt", "r") as f:
      print(f.read())
  ```
- **Key Point:**  
  Always use `with` for safer file operations.

---

## 7. Functions

- **File:** [`functions.py`](functions.py)
- **Concepts:**
  - Create functions: `def`
  - Parameters, return values
  - Scope (local/global)
  - Docstrings for documentation
- **Example:**
  ```python
  def square(x):
      """Return the square of x."""
      return x * x

  print(square(4))
  ```
- **Key Point:**  
  Functions promote code reuse and clarity.

---

## 8. Object-Oriented Programming (OOP)

- **File:** [`objects_classes.py`](objects_classes.py)
- **Concepts:**
  - Classes and object creation
  - Constructor: `__init__`
  - Instance variables and methods
  - Example: `Car` class
- **Example:**
  ```python
  class Car:
      def __init__(self, make, model):
          self.make = make
          self.model = model
      def details(self):
          return f"{self.make} {self.model}"

  mycar = Car("Toyota", "Corolla")
  print(mycar.details())
  ```
- **Key Point:**  
  OOP is for modeling real-world entities and relationships.

---

## 9. Comprehensions & Generators

- **File:** [`comprehensions_generators.py`](comprehensions_generators.py)
- **Concepts:**
  - **List Comprehensions:** Compactly create lists from iterables.
    ```python
    numbers = [1,2,3,4,5,6,7]
    squared = [x**2 for x in numbers if x % 2 == 0]
    ```
  - **Dictionary Comprehensions:** Make dictionaries from iterables.
    ```python
    names = ['Alice', 'Bob', 'Charlie']
    lengths = {name: len(name) for name in names}
    ```
  - **Set Comprehensions:** Build sets with unique elements.
    ```python
    nums = [1,2,2,3,4,4,5,5,6]
    unique_squared = {x**2 for x in nums}
    ```
  - **Generators:**  
    - Yield items one at a time (memory-efficient).
    - Created with functions using `yield` or generator expressions.
    ```python
    def generate_numbers():
        for i in range(1, 10):
            yield i
    for num in generate_numbers():
        print(num)
    ```
- **Key Point:**  
  Comprehensions are concise and expressive; generators save memory for large data.

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

Treat this repository as your living theory book:  
Read the explanations, study the code, and run scripts to experiment. Come back whenever you want to review Python basics or prepare for coding interviews!

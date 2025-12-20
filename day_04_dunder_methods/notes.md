# Dunder (Magic) Methods in Python
## Introduction
Dunder (Magic) Methods in Python are special methods that start and end with double underscores (__).
They enable developers to define how objects behave with built-in Python operations such as printing, comparison, sorting, and function calls.  
These methods are automatically invoked by Python and form the foundation of Python’s object-oriented design.

## What Are Dunder Methods?
- “Dunder” stands for Double UNDERscore
- Used to implement operator overloading
- Allow custom objects to behave like built-in data types.
  
  Example:
```python
print(obj)      # Calls obj.__str__()
obj1 == obj2    # Calls obj1.__eq__(obj2)
```
## 1️⃣`__str__` Method
<u>Purpose</u>
Returns a human-readable string representation of an object.
## When It Is Called
- print(object)
- str(object)
## Use Case 
Used to display meaningful information to users.  
**Example:**
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student(Name={self.name}, Marks={self.marks})"
```
# 2️⃣ `__repr__` Method
<b>Purpose</b>  
Returns an official, unambiguous string representation of an object.

<b>When It Is Called</b>
- Interactive interpreter
- Debugging
- Logging

<b>Best Practice</b>
The returned string should ideally be able to recreate the object.

<b>Example:</b>

# 3️⃣ __eq__ Method (Equality Operator)
**Purpose** <br>
Defines how objects are compared using the == operator.  

**Default Behavior** <br>
Without __eq__, Python compares memory addresses, not values.  

**Example:** <br>
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __eq__(self, other):
        return self.pages == other.pages
```

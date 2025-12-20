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

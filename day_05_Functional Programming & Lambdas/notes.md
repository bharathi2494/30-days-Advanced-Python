# Functional Programming
Functional Programming (FP) is a programming paradigm that emphasizes:  
- The use of pure functions
- Immutability of data
- Avoiding shared state and side effects
Python supports functional programming concepts along with other paradigms such as procedural and object-oriented programming.

In Python, functional programming (FP) is a coding style where you build programs by nesting and combining small, reusable functions rather than focusing on objects or step-by-step instructions (statements).  
Instead of telling the computer how to do something (e.g., using a for loop to manually update a list), you describe what you want the result to be using mathematical-like functions.

## Core Concepts
## 1.Pure Functions:
A function that always gives the same output for the same input and has no "side effects" (it doesn't change global variables or print to the screen). 
```python
def square(x):
    return x * x
```
## 2.Immutability:
Data is not changed after it is created. Instead of modifying a list, you create a new one with the changes. 
```python
numbers = (1, 2, 3)
new_numbers = numbers + (4,)
```
## 3.Functions as First-Class Objects.
In Python, functions are treated as first-class objects, meaning they can be:
- Assigned to variables
- Passed as arguments to other functions
- Returned from functions
```python
def add(a, b):
    return a + b

operation = add
result = operation(3, 4)
```
## Lambda Expressions
A lambda expression is an anonymous function defined using the lambda keyword.
It is typically used for short, simple operations.
**Example:**
```python
square = lambda x: x * x
result = square(5)
```
# Functional Built-in Functions  
## map()
Applies a function to each element of an iterable.
```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
```
## filter()
Filters elements based on a condition.
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```
## reduce()
Applies a rolling computation to combine elements into a single value.
```python
from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, numbers)
```
# When to Use Functional Programming
## Advantages
- Cleaner and concise code
- Easier reasoning and testing
- Reduced side effects
- Better suitability for parallel processing

## Limitations
- Can reduce readability if overused
- Debugging complex lambdas is difficult
- Not ideal for state-heavy logic

# Summary
- Functional programming focuses on functions, immutability, and purity
- Lambda expressions provide concise function definitions
- map(), filter(), and reduce() are core functional tools
- Use lambdas for simple, short-lived logic only



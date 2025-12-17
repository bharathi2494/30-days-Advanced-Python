# Heap vs Stack
## Stack Memory
- Used for function calls and local variables
- Fast but limited size
- Automatically cleared when function ends

## Heap Memory
- Used for objects, lists, dictionaries, classes
- Larger memory, slower than stack
- Stored until no references exist

# Garbage Collection (GC)
- Automatically frees unused memory
- Works via reference counting + cyclic GC
- Helps prevent memory leaks

# Reference Counting
- Every object keeps a count of how many variables point to it
- When count = 0 → object deleted

# Circular Reference
- Occurs when objects reference each other
- GC cannot clean them with reference counting alone
- May cause memory leak

# Cyclic Garbage Collection
- Python detects and cleans circular references
- Breaks cycles to free memory
- Works automatically in Python
  
# Weak References (weakref)
- Reference that does NOT increase reference count
- Useful to break circular references and avoid memory leaks
- Kaypoint: weakref must be used explicitly, it does not work automatically.
  

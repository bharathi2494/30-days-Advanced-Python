Today i learned how python code actually runs internally, instead of writing code blindly.

This day focused on
- Python execution flow
- CPython interpreter
- Bytecode
- PVM (Python virtual machine)
- GIL (Global interpreter lock)
- _pycache_ folder

## how Python executed code.
python doesn't run .py files directly.  
## Executon flow:  
Python Source Code (.py)<br>
&nbsp;&nbsp;&nbsp;&nbsp;↓<br>
Compiled to Bytecode (.pyc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;↓<br>
Executed by Python Virtual Machine (PVM)<br>
- Python first compiles code into bytecode
- Bytecode is platform-independent
- PVM executes bytecode line by line

## CPython
- CPython is the default Python interpreter and it is written in the C language.
- Takes .py file
- Compiles it into bytecode (.pyc)
- Executes the bytecode using the Python Virtual Machine (PVM)

## Bytecode
- Bytecode is a low-level internal representation of Python code
- Stored as .pyc files
- Generated automatically by Python
- Improves performance by avoiding recompilation

## '__Pycache__'
- '__pycache__' is a folder created by Python
- It stores compiled bytecode files (.pyc)
- Helps Python run programs faster next time
- Safe to delete (Python recreates it automatically)

## Python virtual Machine(PVM)
- PVM is a engine that executes Bytecode
- Python code runs inside PVM, not directly on CPU
- PVM reads bytecode instructions one by one.

## Global interpreter lock (GIL)
- GIL is a lock in CPython
- It allows only one thread to execute Python code at a time
- Exists to keep memory management safe
- Limits CPU-bound multithreading

## Key Takeaways
- Python compiles code to bytecode
- Bytecode is executed by PVM
- CPython is the default interpreter
- GIL allows only one thread to execute Python code
- __pycache__ stores compiled bytecode
- Python favors simplicity and safety over raw speed

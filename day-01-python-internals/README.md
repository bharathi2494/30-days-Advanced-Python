Today i learned how python code actually runs internally, instead of writing code blindly.

This day focused on
- Python execution flow
- CPython interpreter
- Bytecode
- PVM (Python virtual machine)
- GIL (Global interpreter lock)
- _pycache_ folder

## how Python executed code.
python doesn't run .py files directly
Executon flow:

Python Source Code (.py)
        ↓
Compiled to Bytecode (.pyc)
        ↓
Executed by Python Virtual Machine (PVM)

- Python first compiles code into bytecode
- Bytecode is platform-independent
- PVM executes bytecode line by line

# CPython
- CPython is the default Python interpreter and it is written in the C language.
- Takes .py file
- Compiles it into bytecode (.pyc)
- Executes the bytecode using the Python Virtual Machine (PVM)

# Bytecode
- Bytecode is a low-level internal representation of Python code
- Stored as .pyc files
- Generated automatically by Python
- Improves performance by avoiding recompilation

# __Pycache__
- __pycache__ is a folder created by Python
- It stores compiled bytecode files (.pyc)
- Helps Python run programs faster next time
- Safe to delete (Python recreates it automatically)

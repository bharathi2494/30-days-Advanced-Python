# lambda based calcuator
calculator={
    'addition': lambda a,b:a+b,
    'substraction': lambda a,b: a-b,
    'multiplication': lambda a,b: a*b,
    'division': lambda a,b: a/b if b!=0 else 'Error'
    }

print(calculator['addition'](20,10))
print(calculator['substraction'](20,10))
print(calculator['multiplication'](20,10))
print(calculator['division'](20,10))
print(calculator['division'](20,0))
#implement map() manually

def my_map(func, iterable):
    result=[]
    for item in iterable:
        result.append(func(item))
    return result

numbers=list(range(1,11))
squares= lambda x: x*x

results=my_map(squares, numbers)
print(results)
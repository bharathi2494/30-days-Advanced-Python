# Ex 1: Filter & Transform at the Same Time
numbers=[1,2,3,4,5,6,7,8,9,10]
evens=[]
for i in numbers:
    if i%2==0:
        evens.append(i)
print(evens)

# using lambdas:
numbers=[1,2,3,4,5,6,7,8,9,10]
evens=list(map(lambda x:x*x, (list(filter(lambda x:x%2==0, numbers)))))
print(evens)

# Ex 2: Process Dictionary Values
students = {
    "Ravi": 82,
    "Anu": 68,
    "John": 91,
    "Meena": 74
}
passed=[]
for name, marks in students.items():
    if marks>75:
        passed.append(name)
print(passed)

# using lambdas
students = {
    "Ravi": 82,
    "Anu": 68,
    "John": 91,
    "Meena": 74
}
passed=list(map(lambda x:x[0],
                list(filter(lambda x:x[1]>=75, students.items()))))
print(passed)
        
# Ex 3: Clean & Filter Strings
names = ["  ram ", "shyam", "  alexander ", "amy"]
result=[]
for name in names:
    clean=name.strip()
    if len(clean)>4:
        result.append(clean.upper())
print(result)

# using lambdas:
names = ["  ram ", "shyam", "  alexander ", "amy"]

result=list(map(lambda x:x.upper(),
                list(filter(lambda x :len(x)>4, 
                   list(map(lambda x: x.strip(), names))))))
print(result)

# Ex:4 Nested Data
#Task: From a list of employee records, 
# get salary after 10% bonus for employees earning more than 50k.
employees = [
    {"name": "A", "salary": 40000},
    {"name": "B", "salary": 60000},
    {"name": "C", "salary": 80000}
]
updated_salaries=[]
for x in employees:
    if x['salary']>50000:
        updated_salaries.append(x['salary']*1.10)
print(updated_salaries)

# using lambdas:
updates_salaries=list(map(lambda x:x['salary']*1.10,
                          list(filter(lambda x:x['salary']>50000, employees))))

print(updates_salaries)

# Ex 5: Multi-Condition Filtering + Transformation
# task: Keep numbers divisible by 3 and 5, Convert them to strings like "Value: 15"
nums=range(1,101)
result=[]
for i in nums:
    if i%3==0 and i%5==0:
        result.append(f'value:{i}')
print(result)

# using lambda
result=list(map(lambda x: f'value:{x}',
                list(filter(lambda x: x%3==0 and x%5==0, nums))))

print(result)
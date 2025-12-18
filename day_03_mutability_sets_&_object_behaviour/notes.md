## 1️⃣ Mutable vs Immutable

Mutable objects can be changed after creation.  
Examples: list, set, dict

Immutable objects cannot be changed after creation.  
Examples: int, str, tuple, frozenset

## 2️⃣ What is a Set?

A set is an unordered collection that stores only unique values.

s = {1, 2, 2, 3}  
print(s)   # {1, 2, 3}

Properties:
- No duplicates
- Unordered
- Uses hashing internally

## 3️⃣ Why Sets Are Unordered

Sets do not store elements by position (index). They store elements using hash values, so order is not guaranteed.

s = {1, 2, 3, 4}  
print(s)  

Output order may change.

## 4️⃣ Hashing

Hashing converts an object into a fixed-size integer called a hash value.  
Python uses hashing to:
- Store set elements
- Store dictionary keys

## 5️⃣ Hashability (Definition)

Hashability is the property of an object that allows it to have a fixed hash value during its lifetime.  

Only immutable objects are hashable.

## 6️⃣ Why set is NOT Hashable
- A set is mutable
- Elements can be added or removed
- Hash value would change

s = {1, 2, 3}  
hash(s)   # TypeError

## 7️⃣ Why frozenset IS Hashable
- frozenset is immutable
- Contents cannot change
- Safe to generate hash

fs = frozenset({1, 2, 3})  
hash(fs)   # Works

## 8️⃣ Using frozenset as Dictionary Key
student_groups = {}  

group = frozenset(["Alice", "Bob"])  
student_groups[group] = "Group A"  

print(student_groups)

## 9️⃣ id(), is, ==

id() → memory address  

== → value equality  

is → same object in memory  

a = [1, 2]  
b = [1, 2]  
print(a == b)  # True  
print(a is b)  # False  

## 🧠 Key Takeaways
- Sets store unique elements using hashing
- Sets are unordered
- Elements inside sets must be hashable
- set is NOT hashable
- frozenset IS hashable and can be used as dict keys

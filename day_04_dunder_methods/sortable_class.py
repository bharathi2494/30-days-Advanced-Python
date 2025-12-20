class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __str__(self):
        return f"{self.name} - {self.marks}"
    
s1 = Student("Ravi", 85)
s2 = Student("Anu", 92)
s3 = Student("Kiran", 78)

students = [s1, s2, s3]
sorted_students = sorted(students)

for s in sorted_students:
    print(s)

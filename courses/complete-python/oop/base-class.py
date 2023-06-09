class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student1 = Student('John Smith', [70, 88, 90, 97])

print(student1.average())

# Equivalent to
# print(Student.average(student1))

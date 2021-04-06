class Student:

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):

    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 10


alain = WorkingStudent('Alain', 'ABC', 15.50)
print(alain.salary)
alain.marks.append(60)
alain.marks.append(80)
print(alain.average())
print(alain.weekly_salary)

john = Student('John', 'DEF')
john.marks.append(66)
john.marks.append(95)
print(john.average())

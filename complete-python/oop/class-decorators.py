class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


john = Student('John', 'MIT')
john.marks.append(79)
john.marks.append(87)
print(john.average())


class SillyClass:

    def __init__(self, name):
        """
        This is a magic method and an instance method as well
        """
        self.name = name

    @classmethod
    def hello(cls):
        return f'Hello {cls.__name__}'

    @staticmethod
    def whats_the_weather():
        return f'Always sunny'


print(SillyClass.hello())
print(SillyClass.whats_the_weather())


class FixedFloat:

    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

new_num = FixedFloat.from_sum(19.575, 0.789)
print(new_num)


class Euro(FixedFloat):

    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro.from_sum(16.758, 9.999)
print(money)

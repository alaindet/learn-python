grades = [80, 75, 90]

grades.append(100)

total = sum(grades)
length = len(grades)

average = total / length

grades_as_strings = [ str(grade) for grade in grades ]
grades_as_string = ', '.join(grades_as_strings)
print(f'Grades are: {grades_as_string}')

print(f'Average is {average}')

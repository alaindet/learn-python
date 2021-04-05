def divide(a, b):
  """
  This could become a lambda function
  """
  return a / b

divide_as_lambda = lambda x, y: x / y

print(divide_as_lambda(7, 4)) # 1.75

# Ex 2
# Declare lambda, call it, return its result then destroy it
# They are called IIFE in JavaScript
immediately_call = (lambda a, b: a + b)(5, 6)
print(immediately_call) # 11


# Ex 3
students = [
  {'name': 'Alice', 'grades': (80, 90, 100)},
  {'name': 'Bob', 'grades': (86, 84, 90)},
  {'name': 'Charlie', 'grades': (79, 80, 100)},
]


average = lambda sequence: sum(sequence) / len(sequence)

for student in students:
  print(average(student['grades']))

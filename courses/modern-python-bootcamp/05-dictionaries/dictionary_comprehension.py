nums = dict(first=1, second=2, third=3)
squared_nums = {key: val**2 for key, val in nums.items()}
print(squared_nums)  # {'first': 1, 'second': 4, 'third': 9}

d1 = {f'k{n}': n**2 for n in range(1, 5)}
print(d1)  # {'k1': 1, 'k2': 4, 'k3': 9, 'k4': 16}

s1 = 'abc'
s2 = '123'
d2 = {s1[i]: s2[i] for i in range(len(s1))}
print(d2)  # {'a': 1, 'b': 2, 'c': 3}

# Using conditionals
d3 = {n: ('even' if n % 2 == 0 else 'odd') for n in range(1, 5)}
print(d3)  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

d4 = {f'k{n}': n for n in range(1, 5) if n % 2 == 0}
print(d4)  # {'k2': 2, 'k4': 4}

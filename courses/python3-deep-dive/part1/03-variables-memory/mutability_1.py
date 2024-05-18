def describe(message, the_variable):
    print(f'{message}:', hex(id(the_variable)))


a = 10
describe('a = 10', a)  # a = 10: 0x7ffb4342e448

a = 15
describe('a = 15', a)  # a = 15: 0x7ffb4342e4e8

# Here, assigning the same literal to different variables gives them
# the SAME memory address as the literal itself
b = 42
c = 42
describe('b = 42', b)  # b = 42: 0x7ffb4342e848
describe('c = 42', c)  # c = 42: 0x7ffb4342e848 <-- Same
describe('42', 42)     # 42:     0x7ffb4342e848 <-- Same

# A list, as well as all compound types, is mutable
# So, "mutating" a list leaves the it at the same memory address
a = [1, 2, 3]
describe('a = [1, 2, 3]', a)     # a = [1, 2, 3]:    0x1f72e505700
a.append(4)
describe('a = [1, 2, 3, 4]', a)  # a = [1, 2, 3, 4]: 0x1f72e505700 <-- Same

print('\n----- Tuples -----')

# This is a tuple (immutable) with numbers (immutable)
t1 = (1, 2, 3)
describe('t1 = (1, 2, 3)', t1)  # t1 = (1, 2, 3): 0x1cd54b6ef80

# This is a tuple (immutable) with lists (mutable)
t2 = ([1, 2], [3, 4])
t2_0, t2_1 = t2
describe('t2', t2)  # t2: 0x1581ca5f780
describe('t2_0', t2_0)  # t2_0: 0x1581ca47e80
describe('t2_1', t2_1)  # t2_1: 0x1581ca5f0c0

# Here, we MUTATED the first element of the tuple, but all addresses stay the same
t2_0.append(10)
describe('t2', t2)  # t2: t2: 0x1581ca5f780
describe('t2_0', t2_0)  # t2_0: 0x1581ca47e80
describe('t2_1', t2_1)  # t2_1: 0x1581ca5f0c0

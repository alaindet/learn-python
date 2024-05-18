def describe(the_message, the_variable):
    print(f'{the_message}:', hex(id(the_variable)))


list1 = [1, 2, 3]
describe('list1', list1)  # 0x1e310d45700

# This modifies list1 internally and does not change its memory address
list1.append(4)
describe('list1 modified internally', list1)  # 0x1e310d45700

# This sums list1 to another literal list and moves the result to a new memory
# address which is then labelled "list1" again, while the old memory address
# of "list1" will be garbaged collected
list1 = list1 + [5]
describe('list1 added', list1)  # 0x1e310edeb40

tuple1 = ([1, 2], [3, 4])
describe('tuple1', tuple1)        # 0x1cb4cd7f3c0
describe('tuple1[0]', tuple1[0])  # 0x1cb4cb85700
describe('tuple1[1]', tuple1[1])  # 0x1cb4cd67e80

# All memory addresses stayed the same, but the internal state of tuple1[0]
# was changed
tuple1[0].append(42)
describe('tuple1', tuple1)        # 0x1cb4cd7f3c0
describe('tuple1[0]', tuple1[0])  # 0x1cb4cb85700
describe('tuple1[1]', tuple1[1])  # 0x1cb4cd67e80

# This is not possibile and raises a TypeError
# TypeError: 'tuple' object does not support item assignment
# tuple1[0] = tuple1[0] + [69]

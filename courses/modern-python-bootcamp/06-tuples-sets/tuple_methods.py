nums = (1, 2, 3, 3, 3)

print(nums.count(3))  # 3
print(nums.count(42))  # 0

print(nums.index(3))  # 2 (first occurrence)

try:
    print(nums.index(42))
except ValueError:
    print('You provided a non-existing value')

print(2 in nums)  # True
print(42 in nums)  # False

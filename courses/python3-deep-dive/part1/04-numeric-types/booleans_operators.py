a = [1, 2, 3]
b = {'a': 1, 'b': 2}
c = 42

# Returns the value of b, not a boolean!
print('a and b:', a and b)  # {'a': 1, 'b': 2}

# If a is falsy, it returns the value of a, not False!
print('None and b:', None and b)  # None <-- This is the left operand value

# In a chain of and, either False or the value of the last expression is returned
print('a and b and c:', a and b and c)  # 42
print('a and False and c:', a and False and c)  # False

# Returns the value or a, not a boolean!
print('a or b:', a or b)  # [1, 2, 3]

print('False or 42:', False or 42)  # 42

# In a chain of or, either False or the value of the first truthy expression is returned
print('a or b or c:', a or b or c)  # [1, 2, 3]
print('False or b or c:', False or b or c)  # {'a': 1, 'b': 2}

s1 = None
s2 = ''
s3 = 'abc'

print('First character of s1:', s1 and s1[0] or '<empty>')  # <empty>
print('First character of s2:', s2 and s2[0] or '<empty>')  # <empty>
print('First character of s3:', s3 and s3[0] or '<empty>')  # a

a = 42

print('Ref of "a":', id(a)) # 140722027613912

# This is equivalent of the above, but in hexadecimal format
print ('Hex ref of "a":', hex(id(a))) # 0x7ffc6677ced8

# The 42 literal has a reference which is the same as "a" as stays constant as
# 42 is a contant value
print('Ref of 42 literal:', id(42)) # 140722027613912
print('Compare refs of "a" and 42:', id(a) == id(42)) # True

a += 1
print('Ref of "a" post-increment:', id(a)) # 140722027613944
print('Ref of 43 literal:', id(43)) # 140722027613944
print('Compare refs of "a" and 43:', id(a) == id(43)) # True

b = a
print('a:', id(a), 'b:', id(b), 'equal?:', id(a) == id(b))
a += 1
print('[Post-increment] a:', id(a), 'b:', id(b), 'equal?:', id(a) == id(b))
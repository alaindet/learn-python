print(int(42))  # 42
print(int(-42))  # -42
print(int(6.666))  # 6 (truncation happens, not math.floor)
print(int('123'))  # 123, base 10 assumed
print(int('1010', 2))  # 10, base 2 explicited

# More explicit via keyword arguments
print(int('1010', base=2))  # 10, base 2 explicited

print(int('f0f', base=16))  # 3855
print(int('F0F', base=16))  # 3855

# The explicit numeric bases can be at most equal to 36, which is the result of
# 10 digits
# 26 letters

# Using an invalid "digit" for the given base
try:
    print(int('a', base=10))
except ValueError as err:
    print(err)  # invalid literal for int() with base 10: 'a'

print(int('31', base=8))  # 31 oct = 25 dec LOL

# From decimal to other bases
print(bin(42))  # 0b101010
print(oct(42))  # 0o52
print(hex(42))  # 0x2a

# Declaring literal integers with different bases
a = 0b101010  # base 2
b = 0o52  # base 8
c = 0x2a  # base 16
d = 42  # base 10

print(a == b, b == c, c == d)  # True True True


def change_base(n: int, b: int) -> str:
    lettersMap = '0123456789abcdefghijklmnopqrstuvwxyz'

    if b < 2 or b > len(lettersMap) or n < 0:
        raise ValueError('invalid inputs')

    if n == 0:
        return [0]

    digits = []
    while n > 0:
        m = n % b
        n = n // b
        digits.insert(0, m)

    return ''.join([lettersMap[d] for d in digits])


print(change_base(42, 16))  # 2a

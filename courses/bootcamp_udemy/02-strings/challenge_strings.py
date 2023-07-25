import math

# Challenge 1
cli_output = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
mac_address = cli_output.split()[-1] # b4:6d:83:77:85:f3
print(mac_address)

# Challenge 2
# ...

# Challenge 3
# value_ft = float(input('Enter a value in ft: '))
# value_cm = value_ft * 30.48
# print(f'{value_ft:.2f} ft = {value_cm:.2f} cm')

# Challenge 4
def is_palindrome(raw_str: str) -> bool:
    processed = raw_str.strip().replace(' ', '').lower()
    return processed == processed[::-1]

print(is_palindrome('itopinonavevanonipoti')) # True

# Challenge 5
print(is_palindrome('I topi non avevano nipoti')) # True

# Challenge 6
def word_ends(s: str, left_len = 2, right_len = 2) -> str:
    return s[0:left_len] + s[-right_len:]

print(word_ends('Together')) # Toer
print(word_ends('Together', 1, 1)) # Tr
print(word_ends('Together', 3, 3)) # Togher
print(word_ends('Together', 100, 100)) # TogetherTogether

# Challenge 7
def change_first(s: str, change_with = '$') -> str:
    first_char = s[0]
    return first_char + s[1:].replace(first_char, change_with)

print(change_first('success', '$')) # succe$$

# Challenge 8
def remove_nth(s: str, i: int) -> str:
    if s == '':
        return s
    return s[0:i] + s[i+1:]

print(remove_nth('hello', 2)) # helo

# Challenge 9
def remove_odd_chars(s: str) -> str:
    return s[::2]

print(remove_odd_chars('axbxcxdx')) #abcd

# Challenge 10
def circle_area(radius: float) -> float:
    return radius * radius * 2 * math.pi

radius = float(input('Enter the circle\'s radius: '))
area = circle_area(radius)
print(f'Circle radius = {radius:.4f}, Circle area = {area:.4f}')
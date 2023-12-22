# Conditionals
- In Python, conditionals use the keywords `if`, `elif` and `else`
- Usually, `if` is the only thing you need, `else` comes second at a far distance, if you use `elif` you really have to question what you're doing; same thing applies for any programming language
- Example
```py
x = 10
if x <= 10:
    print('X is less or equal to 10.')
elif x == 10:
    print('X is exactly 10.')
else:
    print('X is definetely greater than 10.')
```
- **NOTE**: If 2+ branches match in the same if chain, only **THE FIRST** matching branch executes
- For example, in the code above `print('X is exactly 10.')` will never execute since it overlaps with the condition proceeding it
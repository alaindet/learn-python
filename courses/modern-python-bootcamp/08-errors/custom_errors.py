try:
    # A built-in error raised programmatically by user code
    raise ValueError('Some extra info')
except ValueError as err:
    print('ValueError:', err)
    # ValueError: Some extra info

def color_text(text: str, color: str) -> str:

    colors_whitelist = 'red', 'green', 'blue'

    # Runtime type checking
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    
    if color not in colors_whitelist:
        raise ValueError('invalid color')

    return f'Here is "{text}" colored in {color}'

# Prints
# ValueError: Some extra info
# TypeError: text must be a string
# Finally happening.
try:
    color_text(123, 'red') # Raises TypeError
    color_text('hello world', 'purple') # Raises ValueError
    print(color_text('hello', 'green')) # It's fine
except TypeError as err:
    print('TypeError:', err)
except ValueError as err:
    print('ValueError:', err)
finally:
    print('Finally happening.')


# Complete syntax example -----------------------------------------------------
    
# Example 1 with no error
try:
    print('1. This runs undisturbed')
except Exception:
    print('This never runs since no error occurs in try block')
else:
    print('2. This runs after try, but ONLY when except block doesn\'t run')
finally:
    print('3. This runs always, anyway')

# Example 2 with error
try:
    print('1. This runs undisturbed')
    foo # <-- Code stops here
    print('This never runs')
except Exception:
    print('2. This runs since a NameError occurred in try block')
else:
    print('This never runs as try block failed')
finally:
    print('3. This runs always, anyway')


# Capturing multiple errors with the same except block
try:
    print(10/0)
    print(a/0)
except (ZeroDivisionError, NameError) as err:
    print('ZeroDivisionError or NameError:', err)


# Capturing multiple errors with multiple except blocks
try:
    print(10/0)
    print(a/0)
except ZeroDivisionError as err:
    print('ZeroDivisionError:', err)
except Exception as err:
    print('NameError:', err)

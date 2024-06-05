"""
A closure is the combination of a function bundled together (enclosed) with
references to its surrounding state (the lexical environment). In other words,
a closure gives you access to an outer function's scope from an inner function.

Python creates an intermediary object in memory called a "cell" for each variable
that is shared between two local scopes. The cell then "survives" the destruction
of scopes, if it's still referenced

A much more developer-friendly, slightly inaccurate definition of a closure:
- A closure is an inner function bound to its parent function's scope
- "Free variables" are variables "freed" of their local scope and surviving via cells
"""

def outer():
    """
    What happens here is x is referenced by "outer" and "inner" local scopes, so
    Python stores it in a "cell" object.
    
    When the "outer" local scope dies the "x" variable is supposed to be garbage
    collected; but, since the "inner" function is returned, it can still be called
    later and access "x": in this case Python stores "x" in a cell, saving it from
    the destruction of the "outer" local scope which created it.
    """
    x = 42
    def inner():
        print(x)
    return inner

# Example with a counter
def create_counter(initial_value = 0):
    """
    Another example of a cell. "counter" is stored in a cell and later referenced
    whenever you call "count()" later from the global scope
    """
    counter = initial_value

    def count():
        nonlocal counter
        counter += 1
        return counter
    
    return count

c = create_counter(2)
print(c()) # 3
print(c()) # 4
print(c()) # 5
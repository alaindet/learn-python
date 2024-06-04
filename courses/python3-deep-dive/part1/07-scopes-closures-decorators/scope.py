def define_global_foo():
    """This function declares/overrides a global variable foo"""
    global foo
    foo = 42


# Weird but ok. Please, don't do this
define_global_foo()
print(foo)


for i in range(10):
    x = 2 * i

# WARNING: block scopes like other languages do not exist, but PLEASE do not
# exploit this. Treat x as if it doesn't exist outside of the loop
print(x)  # Prints 18

import inspect
from inspect import isfunction, ismethod, isroutine


def foo():
    print('foo')
    pass


class TheClass:
    def foo(self):
        print('TheClass.instance.foo')
        pass


obj = TheClass()

# Checks if it's a first-class function
print('isfunction(foo)', isfunction(foo))  # True
print('isfunction(obj.foo)', isfunction(obj.foo))  # False

# Checks if it's an instance method
print('ismethod(foo)', ismethod(foo))  # False
print('ismethod(obj.foo)', ismethod(obj.foo))  # True

# Checks if it's a function or a method
print('isroutine(foo)', isroutine(foo))  # True
print('isroutine(obj.foo)', isroutine(obj.foo))  # True

# Get the code from other code
print(inspect.getsource(foo))
# Prints
# def foo():
#     print('foo')
#     pass

print(inspect.getmodule(foo))  # <module '__main__' [...]>


def bar(a, b, *args, c, d, **kwargs):
    pass


print(inspect.signature(bar))  # (a, b, *args, c, d, **kwargs)

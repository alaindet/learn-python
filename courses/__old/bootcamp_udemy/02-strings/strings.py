"""The module's docstring"""

a_string = 'Hello World'
another_string = "Hello again"

single_with_double = 'He said "Wow!"'
single_with_single = 'He then said \'That\'s amazing\''

double_with_single = "This is technically 'a bug'"
double_with_double = "You cannot say \"I'm sorry\" without meaning it"

print(type(a_string)) # <class 'str'>

def hello():
    """This is hello's docstring"""
    pass

print(hello.__doc__) # Outputs "This is hello's docstring"

print(__doc__) # Outputs "The module's docstring"

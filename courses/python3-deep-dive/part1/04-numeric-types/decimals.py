"""
Doing multiple imports from the same module is "fine" for prototyping
Here, we both need the Decimal class inside the decimal module
and the decimal module per se as a dictionary to do something like decimal.getcontext()
"""
import decimal
from decimal import Decimal

print(decimal.getcontext())
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
#    capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero,
#    Overflow])

# You can change the global context like this
decimal.getcontext().prec = 4
print(decimal.getcontext())
# Context(prec=4, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
#    capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero,
#    Overflow])

# Better
g_ctx = decimal.getcontext()
g_ctx.prec = 4
print(type(g_ctx)) # <class 'decimal.Context'>
print(g_ctx) # As print(decimal.getcontext())

# What if you need to change the context just for a small amount of instructions?
# Local context is a copy of the global context which you can use and discard
# via context managers

a = Decimal('1.25')
b = Decimal('1.35')

with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_CEILING
    # Here, we're using a custom rounding algorithm for this local context
    print('local context', round(a, 1)) # local context 1.3
    print('local context', round(b, 1)) # local context 1.4

# The local context gets discarded and the global context is used instead
# so the rounding algorithm
print('global context', round(a, 1)) # global context 1.2
print('global context', round(b, 1)) # global context 1.4

# -----------------------------------------------------------------------------
#
# IMPORTANT
# 
# -----------------------------------------------------------------------------

# Instantiating a Decimal with a float literal is an error since you're storing
# an already approximate value
a = Decimal(0.1) # NOPE
b = Decimal('0.1') # OK

print(a) # 0.1000000000000000055511151231257827021181583404541015625
print(b) # 0.1

# You can also instantiate Decimal using a tuple with three values
# - The sign (0 for positive or zero and 1 for negative)
# - A nested tuple with significant digits
# - The exponent of base 10
#
# For example, -1234e-4 is
sign = 1
digits = (1, 2, 3, 4)
exp = -4
c = Decimal((sign, digits, exp))
print(c) # -0.1234

"""
# Decimal precision

The precision you defined in a decimal context *only affects operations*, meaning
any decimal that you instantiate has its own number of decimals stored as needed
Then, when you use decimals to perform operations the defined precision of the
context gets used
"""

# Here, only c is affected by the selected precision, while a and b stay the same
with decimal.localcontext() as ctx:
    ctx.prec = 1
    a = Decimal('0.12345')
    b = Decimal('0.12345')
    c = a + b
    print(a, b, c) # 0.12345 0.12345 0.2

    ctx.prec = 3
    a = Decimal('0.12345')
    b = Decimal('0.12345')
    c = a + b
    print(a, b, c) # 0.12345 0.12345 0.247
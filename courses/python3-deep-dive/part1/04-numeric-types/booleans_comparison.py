"""
## Comparisons

They're all binary operations and always evaluate to a boolean
- Identity (is)
- Equality (==, !=)
- Ordering (>, >=, <, <=)

- Identity only works when objects have the same address
- Equality works with all numbers except for floats (due to approximation)
- Ordering works with all numbers, expect complex ones
"""

import math
from decimal import Decimal
from fractions import Fraction


if 3 < math.pi < 4:
    print('PI is between 3 and 4')

# Equivalent to
if 3 < math.pi and math.pi < 4:
    print('PI is between 3 and 4')

if 1 < 2 < 3 < 4 < 5:
    print('Integers are ordered, as expected')

# Equivalent to
if 1 < 2 and 2 < 3 and 3 < 4 and 4 < 5:
    print('Integers are ordered, as expected')

if 1 + 1 is 2:
    print('1+1 and 2 are identical, not just equal')

if 0.1 > Decimal('0.1'):
    print('0.1 float representation is greater then exact 0.1')

if True == Fraction(42, 42):
    print('True is 42/42')

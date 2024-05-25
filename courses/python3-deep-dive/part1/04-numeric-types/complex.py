"""
Complex numbers are a primitive type in Python, created via literals or complex()
The module "cmath" is to be used with complex numbers, not "math"
"""
import cmath
import math

# A complex number literal
a = 4 + 5j

# A complex number created via complex() constructor
b = complex(4, 5)

print(a, b, a == b)  # (4+5j), (4+5j), True

# Please notice those are floats even though we provided integers
print(a.real, b.real)  # 4.0 4.0
print(a.imag, b.imag)  # 5.0 5.0
print(a.conjugate(), b.conjugate())  # (4-5j) (4-5j)

# Basic arithmetic works as expected
print(a == b)  # True
print(a != b)  # False
print(a + b)  # (8+10j)
print(a - b)  # 0j
print(a * b)  # (-9+40j)
print(a / b)  # (1+0j)
print(a ** 3)  # (-236+115j)

# Not supported operations
# divmod()
# integer division //
# module %
# anything from the "math" module

# Considering a complex number as a segment in the complex plane, the "phase" is
# the angle of the segment and the "magnitude" is the length of the segment
#
# (https://en.wikipedia.org/wiki/Complex_plane)

# a angle in radiants: 0.8960553845713439
print('a angle in radiants:', cmath.phase(a))

# a length: 6.4031242374328485
print('a length:', abs(a))

# Creating a complex number from magnitude and radiants
angle = 0.8960553845713439
magnitude = 6.4031242374328485
c = cmath.rect(magnitude, angle)
print(c)  # (4+4.999999999999999j)

# (1.0000000000000002+1.0000000000000002j)
print(cmath.rect(math.sqrt(2), math.pi/4))

# Euler's identity (https://en.wikipedia.org/wiki/Euler%27s_identity)
# This should be zero as per Euler's identity. It is very small due to floats
print(cmath.exp(cmath.pi * 1j) + 1)  # 1.2246467991473532e-16j

# cmath.isclose to the rescue
zero = 0
almost_zero = cmath.exp(cmath.pi * 1j) + 1
very_small_tolerance = 1e-15
print(cmath.isclose(zero, almost_zero, abs_tol=very_small_tolerance))  # True

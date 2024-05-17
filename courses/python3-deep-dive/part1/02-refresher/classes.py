class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __str__(self):
        return f'Rectangle: width={self.width}, height={self.height}'
    
    # This should "show" how to build this instance again
    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented

        return (self._width, self._height) == (other._width, other._height)
    
    # This implements "less than" binary operation
    # There are many other "magic methods"
    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self.area() < other.area()
    
    # Idiomatic property getter for width
    @property
    def width(self):
        return self._width
    
    # Idiomatic property setter for width
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('width must be a positive integer')
        self._width = width

    # Idiomatic property getter for height
    @property
    def height(self):
        return self._height
    
    # Idiomatic property setter for height
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('height must be a positive integer')
        self._height = height

    def area(self):
        return self._width * self._height
    
    def perimeter(self):
        return 2 * (self._width + self._height)
    
r1 = Rectangle(3, 5)
r2 = Rectangle(3, 5)
r3 = Rectangle(4, 6)

area = r1.area()
print(f'Area: {area}') # Area: 15

perimeter = r1.perimeter()
print(f'Perimeter: {perimeter}') # Perimeter: 16

# Without a __str__ method
# print(str(r1))
# # <__main__.Rectangle object at 0x000001EEF3CF6690>

# Using the  __str__ method
print('__str__:', str(r1)) # Rectangle: width=3, height=5

# Using the  __repr__ method
print('__repr__:', repr(r1)) # Rectangle(3, 5)

# Using the __eq__ method
print('Comparing with equal Rectangle:', r1 == r2) # True
print('Comparing with diffenrent Rectangle:', r1 == r3) # False

# This returns False as "other" is not a Rectangle instance
print('Comparing with non-Rectangle: ', r1 == [1, 2, 3]) # False

print('Less than:', r1 < r3) # True

# MAGIC HERE: __gt__ does not exist so Python flips the expression
# And uses __lt__
print('Greater than:', r1 > r3) # False

try:
    r1.width = -10
except ValueError as err:
    print(err)
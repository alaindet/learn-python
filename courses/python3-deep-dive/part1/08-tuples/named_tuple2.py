from collections import namedtuple

Point2D = namedtuple('Point2D', ['x', 'y'])
Point3D = namedtuple('Point3D', ['x', 'y', 'z'])

p2d_1 = Point2D(10, 20)
p2d_2 = Point2D(15, 25)
print(p2d_1) # Point2D(x=10, y=20)

p3d_1 = Point3D(1, 2, 3)
p3d_2 = Point3D(4, 5, 6)
print(p3d_1) # Point3D(x=1, y=2, z=3)

def dot_product_3d(a: Point3D, b: Point3D) -> int:
    """This only works with Point3D instances"""
    return sum([z[0] * z[1] for z in zip(a, b)])
    # return a.x * b.x + a.y * b.y + a.z * b.z # Equivalent

print(dot_product_3d(p3d_1, p3d_2)) # 32

def dot_product(a: Point2D | Point3D, b: Point2D | Point3D) -> int:
    """This works both with Point2D and Point3D instances"""
    return sum([z[0] * z[1] for z in zip(a, b)])

print(dot_product(p2d_1, p2d_2)) # 650
print(dot_product(p3d_1, p3d_2)) # 32

Circle = namedtuple('Cicle', ['center_x', 'center_y', 'radius'])

c1 = Circle(radius=10, center_x=0, center_y=0)
print(c1) # Cicle(center_x=0, center_y=0, radius=10)

# Print fields from the namedtuple
print(Circle._fields)

print(help(Circle))
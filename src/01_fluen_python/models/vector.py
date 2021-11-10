from math import hypot # hypot = hypotenuse

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # repr = representation.
    # Returns the string representation of the vector
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    # Returns: Multidimensional Euclidean distance from the origin to a point.
    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)
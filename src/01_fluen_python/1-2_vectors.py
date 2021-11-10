from models.vector import Vector

## vector instances
v1 = Vector(2, 4)
v2 = Vector(2, 1)

# Due to the __repr__ method, string representation is possible
print(f'v1 + v2: {v1 + v2}')

# Absolute number
print(f'abs: {abs(Vector(3, 4))}')

# Multiplication
print(f'v1 * 2: {v1 * 2}')

# Testing bool
print(f'bool: {bool(v2)}')
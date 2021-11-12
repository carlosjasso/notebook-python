from collections import namedtuple
from helpers.string_formatter import print_marked_string

# Example 2-9 shows how we could define a named tuple to hold information about a city
print_marked_string("Example 2-9")

# Instances of a class that you build with namedtuple take exactly the
# same amount of memory as tuples because the field names are stor‐
# ed in the class. They use less memory than a regular object because
# they do store attributes in a per-instance __dict__.
City = namedtuple("City", "name country population coordinates")

tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
print(tokyo)

# Example 2-10. Named tuple attributes and methods
print_marked_string("Example 2-10")

LatLong = namedtuple("LatLong", "lat long")

print(f"City fields: {City._fields}")
delhi_data = ("Dehli NCR", "IN", 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(f"Delhi as dictionary: {delhi._asdict()}")
for key, value in delhi._asdict().items():
    print(f"{key}: {value}")
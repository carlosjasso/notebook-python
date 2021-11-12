from helpers.string_formatter import print_marked_string

# Example 2-7. Tuples used as records.
# Tuples can be seen as immutable lists or records with no field names

# Data about Tokyo: name, year, population (millions), population change (%),
# area (km²).
city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)

traveler_ids = [
    ('USA', '31195855'), 
    ('BRA', 'CE342567'), 
    ('ESP', 'XDA205856')]
print_marked_string("passports")
for passport in sorted(traveler_ids):
    # The % formatting operator understands tuples and treats each item as a separate field.
    print("%s/%s" % passport)

print_marked_string("unpacked tupple")
# The % formatting operator understands tuples and treats each item as a separate
# field.
for country, _ in traveler_ids:
    print(country)

# Latitude and longitude of the Los Angeles International Airport
print_marked_string("unpacked lax")
lax_coordinates = (33.8425, -118.408056)
lat, long = lax_coordinates # tuple unpacking
print(f"lat: {lat}, long: {long}")

# Tuple -  grabbing excess items
print_marked_string("tuple - excess items")
t = (20, 8)
quotient, remainder = divmod(*t)
print(f"quotient: {quotient}, remainder: {remainder}")

a, b, *rest = range(5)
print("range items: ", a, b, rest)
a, b, *rest, c, d = range(10)
print("range items: ", a, b, rest, c, d)

# Example 2-8. Unpacking nested tuples to access the longitude.
print_marked_string("metro stations")
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
template = "{:15} | {:9.4f} | {:9.4f}"
print("{:15} | {:^9} | {:^9}".format("city", "lat", "long"))
for name, cc, pop, (lat, long) in metro_areas:
    print(template.format(name, lat, long))


from helpers.string_formatter import mark_string

# Example 2-7. Tuples used as records.
# Tuples can be seen as immutable lists or records with no field names

# Latitude and longitude of the Los Angeles International Airport
lax_coordinates = (33,8425, -118.408056)

# Data about Tokyo: name, year, population (millions), population change (%),
# area (km²).
city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)

traveler_ids = [
    ('USA', '31195855'), 
    ('BRA', 'CE342567'), 
    ('ESP', 'XDA205856')]
print(mark_string("passports"))
for passport in sorted(traveler_ids):
    # The % formatting operator understands tuples and treats each item as a separate field.
    print("%s/%s" % passport)

print(mark_string("unpacked tupple"))
# The % formatting operator understands tuples and treats each item as a separate
# field.
for country, _ in traveler_ids:
    print(country)


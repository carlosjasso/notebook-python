import array

# genexp = generator expressions

symbols = "$¢£¥€¤"

# Example 2-5 shows basic usage of genexps to build a tuple and an array.
print(f"tuple: {tuple(ord(s) for s in symbols)}")
print(f"array: {array.array('I', (ord(s) for s in symbols))}")

# Example 2-6: uses a genexp with a cartesian product to print out a roster of t-shirts of
# two colors in three sizes. In contrast with Example 2-4, here the 6-item list of t-shirts is
# never built in memory: the generator expression feeds the for loop producing one item
# at a time. If the two lists used in the cartesian product had a thousand items each, usinga generator expression would save the expense of building a list with a million items
# just to feed the for loop.
colors = ["black", "white"]
sizes = ["S", "M", "L"]
for tshirt in ("%s %s" % (c, s) for c in colors for s in sizes):
    print(tshirt)
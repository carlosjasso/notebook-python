# list-comp = list comprenhension

symbols = "$¢£¥€¤"

# List comprenhensions and readability
# Example 2-1. Build a list of Unicode codepoints from a string.
codes = []
for symbol in symbols:
    codes.append(ord(symbol)) # ord(): char to int
print(f"good old for loop: {codes}")

# Example 2-2. Build a list of Unicode codepoints from a string, take two.
codes = [ord(symbol) for symbol in symbols] # list-comp
print(f"listcomp: {codes}")

# Example 2-3: filter+map vs list-comp
codes = list(filter(lambda c: c > 127, map(ord, symbols)))
print(f"filter+map: {codes}")

codes = [ord(s) for s in symbols if ord(s) > 127]
print(f"listcomp: {codes}")

# Example 2-4: Cartesian product
colors = ["black", "white"]
sizes = ["S", "M", "L"]
tshirts = []

for c in colors:
    for s in sizes:
        tshirts.append((c, s))
print(f"Cartesian product  - Nested for: {tshirts}")

tshirts = [(c, s) for c in colors for s in sizes]
print(f"Cartesian product - listcomp: {tshirts}")
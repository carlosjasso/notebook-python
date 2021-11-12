from helpers.string_formatter import print_marked_string

print_marked_string("list slicing")
l = [10, 20, 30, 40, 50, 60]
print(f"list: {l}")
print(f"slice :2 - {l[:2]}")
print(f"slice 2: - {l[2:]}")
print(f"slice :3 - {l[:3]}")
print(f"slice 3: - {l[3:]}")

print_marked_string("string slicing")
s = "bicycle"
print(f"slice ::3 - {s[::3]}") # from x, to y, step 3
print(f"slice ::-1 - {s[::-1]}") # from end to start, step 1
print(f"slice ::-2 - {s[::-2]}") # from end to start, step 2

# Example 2-11. Line items from a flat file invoice
print_marked_string("2-11 string slicing")
invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""
sku = slice(0, 6)
descr = slice(6, 40)
unit_price = slice(40, 52)
qty = slice(52, 55)
total = slice(55, None)

line_items = invoice.split("\n")[2:-1]
for item in line_items:
    print(item[unit_price], item[descr])

# Assigning to slices
print_marked_string("Assigning to slices")
l = list(range(10))
print(f"list: {l}")

l[2:5] = [20, 30]
print(f"\"l[2:5] = [20, 30]\" : {l}")

del l[5:7]
print(f"\"del l[5:7]\" : {l}")

l[2::3] = [11, 22]
print(f'"l[2::3] = [11, 22]" : {l}')
# here's some basics on string opreations

statement = "the quick brown fox jumped over the lazy dog"
money = "$$$$$"

# Length of string

print(f'Length of "{statement}" = { len(statement) }')

# Counting characters/patterns in string

print(f"There's { money.count('$') } dollar signs in {money}")
print(f"There's { money.count('$$') } double-dollar signs in {money}")

# Sub-strings - take the string as an array and declare between indexes with <start>:<stop>

fox = statement[16:19]

print(fox)

# There's also a <start>:<stop>:<step>

dg = statement[41:44:2]
print(dg)

# negative number can also be given to go in reverse

lazy = statement[-8:-4]
print(lazy)

# An easy way to reverse a string - <no-start>:<no-end>:<negative-step>

print(statement[::-1])

# UPPERCASES & lowercases + extra

print(statement.upper())
print(statement.lower())
print(statement.capitalize())

# Check strat or end of string

print(statement.startswith("the"))
print(statement.endswith("dog"))

# String splitting by character

words = statement.split(" ")

print(f"There's {len(words)} words in \"{statement}\"")
# There are different wayt to format strings
# Some basics:
#   %s - String (or any object with a string representation, like numbers or lists)
#   %d - Integers
#   %f - Floating point numbers
#   %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#   %x/%X - Integers in hex representation (lowercase/uppercase)

name = "Donas"
print("Hello %s" % (name)) # old way of formatting
print(f"Hello {name}") # most recent formatting way as of python 3.6

print("A list %s" % ([1, 2, 3, 4]))
print(f"Another list {[5, 6, 7, 8]}")

print("7 same as %.4f" % (7))
print(f"{7} same as {7:.8f}")

# Operators can be used with different types of variables

someResult = 7 * 2 + 5 / 5

print(f'7 * 2 + 5 / 5 = {someResult}')

# modulo is supported

remainder = 20 % 2

print(f'20 % 2 = {remainder}')

# power relationships

squared = 2 ** 2
cubed = 2 ** 3

print(f"2 squared = {squared}")
print(f"2 cubed = {cubed}")

# operators can be used with strings, too

line1 = "Hello" + " " + "world!"
line2 = "money " * 10

print(line1)
print(line2)

# operators can be used even with lists

evenNUmbers = [2, 4, 6, 8]
oddNumbers = [1, 3, 5, 7, 9]
allNumbers = oddNumbers + evenNUmbers
allNumbers.sort()

print(allNumbers)
print(["money"] * 10)
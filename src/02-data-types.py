# Python is completely object oriented, which means that
# no data types have to be declared for every variable.
# All of them are objects

# Numeric variables can hold either integers or decimals

someInt = 114
someDecimal = 3.1416

print(f'someInt: {someInt}')
print(f'someDecimal: {someDecimal}')

# Strings work just as in any other language and are defined with either "" or ''

someString = "Carlos' string"
otherString = 'This is a "string"'

print(someString)
print(otherString)

# Simple operatins can be performed with the variables

print(f"{someInt} + {someDecimal} = {someInt + someDecimal}")

helloString = 'Hello'
worldString = 'world'
helloWorldString = helloString + ' ' + worldString

print(helloWorldString)

# Miltule variable assignment can be done on a single line

aValue, bValue = 1, 2

print(aValue + bValue)

# Operations betwen numbers and strings are not supported

# print(3 + "hello") # Comment or uncomment line for testing


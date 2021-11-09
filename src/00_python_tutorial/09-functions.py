# dunctions are defined witht he "def" keyword
# and have an indented code block that starts with the ":" character

def printHelloWorld():
    print("Hello World!")

# functions can receive params

def printGreeting(name, feeling):
    print(f"Hello, {name}. Hope you're feeling {feeling}")

# receive params and return result

def sumNumbers(a, b):
    return a + b

# calling the functions

printHelloWorld()

printGreeting("Carlos", "Great!")

a = 2
b = 3
print(f"{a} + {b} = {sumNumbers(a, b)}")
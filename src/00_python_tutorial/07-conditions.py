# Python does support boolean logic by making use of the usual operators

x = 2
print(x == 2) # True

y = False

print(y == True) # False
print(y == False) # True
print(x < 5) # True

# if statement. Their code block is delimited by indentation 
# and gets started from the ":" character. 
# Tabs or spaces work

if x == 2 :
    print(f"x = {x}")

# "and" "or" operations

name = "Carlos"
hairStyle = "curly"

if name == "Carlos" and hairStyle == "curly":
    print(f'Your name is "{name}" and you have "{hairStyle}" hair')

if name == "Carlos" or name == "Roger":
    print(f'Your name is either "Carlos" or "Eduardo"')

generalNames = ["Carlos", "Roger", "Smith", "Aaron"]
if name in generalNames:
    print(f'"{name}" is an expected name')

# explicit "not"

bannedNames = ["Roger", "Smith", "Aaron"]
if name not in bannedNames:
    print(f'"{name}" is not a banned name')

# if / else

if x == 2:
    print("X equals 2!")
else:
    print("x is not equal to 2")

# if / else if / else - 
# Use the "pass" keyword for an empty block where nothing is needed to be done

if x == 3.1416:
    print("I love pie!")
elif x == 2:
    print("No pie, huh!")
else:
    print("nada...")

# use "pass" not to break proper indentation when 
# commenting a line

if x == 3.1416:
    pass # if this is not here, code gets broken
    # print("I love pie!")
elif x == 2:
    pass
    # print("No pie, huh!")
else:
    pass

# "Is" operator

if x is y:
    print("X is not Y")

someNoneVar = None

if someNoneVar is None:
    print("That var doesn't have a value")
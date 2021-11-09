# dictionaties are supported and work very similarly as lists
# they get define with a { key : value, key : value } structure
# they are accessed by <name>[key]

phonebook = { "mynumber" : 11111111, "othernumber" : 2222222222 }

print(phonebook["mynumber"])

# iteration

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}

for name, number in phonebook.items():
    print(f"Phone number of {name} is {number}")

# deletion

print("---")

del phonebook["Jack"]
for name, number in phonebook.items():
    print(f"Phone number of {name} is {number}")

# retrieval
print("---")

jill = phonebook.pop("Jill")

for name, number in phonebook.items():
    print(f"Phone number of {name} is {number}")

print(jill)

# conditions

if "John" in phonebook:  
    print("Jhon is listed in the phonebook.")

if "Jack" not in phonebook:  
    print("Jack is not listed in the phonebook.")
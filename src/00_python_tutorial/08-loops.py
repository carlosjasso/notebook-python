# the for loop

# iterate over a given sequence

from typing import List


primes = [2, 5, 7, 9]

for prime in primes:
    print(f"Prime number {List.index(primes, prime)} in sequence is {prime}")

for x in range(5): # range from 0 - 4
    print(x) # Prints out the numbers 0,1,2,3,4

for x in range(3, 6): # range from 3 - 5
    print(x) # Prints out 3,4,5

for x in range(3, 8, 2):# range from 3 - 7, step 2
    print(x) # Prints out 3,5,7

# the while loop

count = 0
while count < 5:
    print(f"{count} / 4")
    count += 1


count = 0
while True: # infinite loop
    if count == 5:
        break
    print(f"{count} / 4") # Prints out 0,1,2,3,4
    count += 1

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    if x % 2 == 0:
        continue
    print(f"{x} is odd")

# else value on a loop!

count=0
while(count<5):
    print(f"{count} is less than 5")
    count +=1
else:
    print("count value reached %d" %(count))

for i in range(1, 10): # range from 1 - 9
    if(i%5==0):
        break
    print(f"{i} % 5 = {i % 5}")
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
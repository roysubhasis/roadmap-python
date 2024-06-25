'''
DAY 4 - Class : Randomization and Python list
'''


## Code 1 - Call a custom lib (Created my_custom_lib.py file and called the same)
import my_custom_lib
print(my_custom_lib.pi_value)


## Code 2 - Random Whlole number generator
import random
reandom_integer = random.randint(1,100) # Generates any random number between 1 to 100 every time the program executes
print(reandom_integer)

## Code 3 - Random Float number generator
import random
reandom_float = random.random() # Generates any random float no between 0.00000000 to 0.99999999
print(reandom_float)


## Task 1 - Random no gen between 0.0000000 to 4.99999999
'''
Now you know Randrom Integer(Code 2) and Random Float(Code 3) Generator.
Based on that learning, 
Generate a  random float no ranging between 0.0000000 to 4.99999999
'''
import random
reandom_float2 = random.random() * random.randint(1,5) # Logic: Random float number multipled by random Integer number will generate a float only
print(reandom_float2)


## Task 2 
'''
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".
There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails

Example Output
Heads
or
Tails
'''
import random
random_side = random.randint(0,1)
if (random_side == 1):
    print("Heads")
else:
    print("Tails")


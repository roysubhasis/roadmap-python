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


## Code 4 - Lists : Data Structure
states_of_america = ["Delaware","Pennsylvania","New Jersey","Georgia","California","Florida","Alaska",
                     "Illinois","Montana","Michigan","Indiana","Texas","New York","Ohio","Hawaii"
                     "Oregon","Kansas","Washington","Maine","Colorado","Nevada"]
print(states_of_america[0])
print(states_of_america[-1])
print(states_of_america[-2])

# Add a state at the end od the list
states_of_america.append("Oklahoma")
print(states_of_america)

# Add/Append few more using extend function
states_of_america.extend(["Tennessee","Louisiana"])
print(states_of_america)


## Task 3
'''
You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.

NOTE: 
In this exercise, you are working collaboratively with another programmer. They already dealt with input() and writing the code needed to get hold of the names in the input area, so you don't need to worry about that.
The other programmer has written the code to separate the names in the input area into individual names and puts them inside a List called names. 
For their code to work correctly, you must enter all the names in the input area followed by comma then space. e.g. name, name, name

You can try printing names to see what it looks like (but remember to remove that code when you submit the assignment).

Assume that names works like this:

input area: x, y, z, 
names = ["x", "y", "z"]

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!

Hints:
You might need the help of the len() function. https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list
Remember that Lists start at index 0!

'''
names_string = "Angela, Ben, Jenny, Michael, Chloe"

#Split the names based on ',' comma
names = names_string.split(", ")

# Get the total number of items in list (length of the list).
num_items = len(names)

# Generate random numbers between 0 and the last index of the list. 
random_choice = random.randint(0, num_items - 1)

# Choose and print a random name from the list.
print(names[random_choice])
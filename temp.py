import random

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




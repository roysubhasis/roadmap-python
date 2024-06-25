'''
DAY 1 - Class : Variables
'''

##Input Functions
print(input("Enter your firstName : "))
print("Hello..." + input("What is your lastName ?") + "..!!")

## Python Variables
name = input("Enter your name : ")
numOfLetters = len(name)
print("no of letter in {0} -> ",name,numOfLetters)

num1=int(input("Enter 1st value : "))
num2=int(input("Enter 2nd value : "))
print("Addition result : ",num1+num2)


## Switch Values of 2 variable
# There are two variables, a and b from input
a = input("Enter 1st value : ")
b = input("Enter 2nd value : ")

print("before switch a is-> " + a);
print("before switch b is-> " + b);

# Switch values
c = a
a = b
b = c

print("After switch a is-> " + a)
print("After switch b is-> " + b)

## Task 1 : Band Name Generator
print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
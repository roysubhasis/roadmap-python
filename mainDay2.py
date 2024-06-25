'''
DAY 2 - Class : Datatypes and Math Operations
'''

## Example of subscript(Pulling a character from a given position)
print("Hello"[0]) 
print("Hello"[4]) 

## Integer
num = 10
print(num+5)

## Float
flt_num=3.141
print(flt_num)

## Boolean
flag = True
print(flag)


##Example 1
numberOfChar = len(input("Type your name : "))
print("your name lengh is " , numberOfChar) # Works
#print("your name lengh is " + numberOfChar) # Gives -> TypeError: can only concatenate str (not "int") to str


print(type(numberOfChar)) #Checking type of data using type function

new_num_char = str(numberOfChar) # Conversion of Integer type data to String
print("your name lengh is " + new_num_char) # Now it should work fine


## Datatype Conversion

a = 123
print(type(a))
print(type(str(a))) #converting Integer to String type

b = 456
print(type(float(b))) #converting Integer to Float type

print(70+float("100.5")) #Addition of int and float

print(str(100)+str(200))

## Task 1
# Problem Stmt : Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input()
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
# Add the two integers together
two_digit_number = first_digit + second_digit
print(two_digit_number)

## Math Operation

print (2**3) # Power operation denoted by ** (double *)

# Order of Priority -> PEMDAS
'''
P -> Parentheses ()
E -> Exponents **
M -> Multiplication *
D -> Division /
A -> Addition +
S -> Subtraction -

# NOTE : Multiplication and Division are of same priority/order, code will execute which ever comes first.

'''
print (3 * 3 + 3 / 3 - 3) # result 7
print (3 * 3 / 3 - 2) # result 1
print (3 * 6 / 3) # result 6
print (27 / 3 * 3) # result 27


## Task 2
'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
BMI Wikipedia Page
The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, 
the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

BMI = weight / suqare of height

Example Input 1
1.75
80
means: weight = 80 and height = 1.75

Example Output 1
26
Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837
'''
height = input("height : ")
weight = input("weight : ")
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
print(int(bmi))

# Using the multiplication
bmi = weight_as_int / (height_as_float * height_as_float) 
print(int(bmi))


## Round the number

print (8/3)  # Output 2.6666666666666665
print (int(8/3)) # Output 2
print (round(8/3)) # Output 3 
print (round(8/3,2)) # Output 2.67 - Round with 2 decimal places
print (round(8/3,3)) # Output 2.667 - Round with 3 decimal places
print (round(2.6666666666666665,2)) # Output 2.67 - Round with 2 decimal places

## FLOW DIVISION using double forward slash (//)

print (8/3) # Gives Float number as result
print (8//3) # Flow division, it gives integer when using double slash (//) after division

print (8/4) # Gives Float number as result
print (8//4) # Flow division, it gives integer when using double slash (//) after division

## Handy way of value manipulation

result = 24/2 
print (result)
result /=2
print (result)


## f-String (Combile different datatype using f-String - Add an 'f' character infrom of string)
score = 0
height = 1.8
isWinning = True

print(f"your score is {score} and your height is {height} and you are winning is {isWinning}") # Example of f-String



## Task 3
'''
I was reading this article by Tim Urban - Your Life in Weeks(https://waitbutwhy.com/2014/05/life-weeks.html) and realised just how little time we actually have.
Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
56

Example Output
You have 1768 weeks left.
'''

age = input("Your current age : ")
yearsLeft = 90 - int(age)
weeksLeft = yearsLeft * 52

print(f"You have {weeksLeft} weeks left.")


## Task 4 - Build a tip calculator

'''
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
'''
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?" ))
people = int(input("How many people to split the bill? "))

#bill_with_tip = tip / 100  * bill + bill
bill_with_tip = round(bill * (1 + tip / 100))
bill_per_person = bill_with_tip / people
final_amt = round(bill_per_person, 2)
print(f"Each person should pay : ${final_amt}")
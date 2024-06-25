'''
DAY 3 - Class : Control Flow and Logical Operators
'''

## Code 1
water_level = 50
if water_level>80:
    print("Drain Water")
else:
    print("Continue filling")


## Code 2 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")


## Task 1 - Find odd or even number
'''
Write a program that works out whether if a given number is an odd or even number.
Even numbers can be divided by 2 with no remainder.
e.g. 86 is even because 86 ÷ 2 = 43
43 does not have any decimal places. Therefore the division is clean.
e.g. 59 is odd because 59 ÷ 2 = 29.5
29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

e.g.
6 ÷ 2 = 3 with no remainder.
therefore: 6 % 2 = 0

5 ÷ 2 = 2 x 2 + 1, remainder is 1.
therefore: 5 % 2 = 1

14 ÷ 4 = 3 x 4 + 2, remainder is 2.
therefore: 14 % 4 = 2

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example 1 Input
43
Example 1 Output
This is an odd number.
'''

number = int(input("Which number do you want to check?"))
reminder = number % 2
if reminder == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


## Task 2 - Body Mass Index (BMI) Interpreter
'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.
'''

height = float(input("Enter your height in meters e.g., 1.55 : "))
weight = int(input("Enter your weight in kilograms e.g., 72 : "))

bmi_value = round(weight / (height**2), 2)
print(float(bmi_value))
if bmi_value < 18.5:
    print(f"Your bmi is {bmi_value}, you are underweight.")
elif bmi_value >=18.5 and bmi_value <25:
    print(f"Your bmi is {bmi_value}, you have a normal weight.")
elif bmi_value >=25 and bmi_value <30:
    print(f"Your bmi is {bmi_value}, you have a slightly overweight.")
elif bmi_value >=30 and bmi_value <35:
    print(f"Your bmi is {bmi_value}, you are obese.")
else:
    print(f"Your bmi is {bmi_value}, clinically obese.")



## Task 3 - Find Leap Year (Nested if-elif)
'''
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 
The reason why we have leap years is really fascinating, this video does it more justice.

This is how you work out whether if a particular year is a leap year.
    on every year that is divisible by 4 with no remainder
    except every year that is evenly divisible by 100 with no remainder
    unless the year is also divisible by 400 with no remainder

If english is not your first language or if the above logic is confusing, try using this flow chart .
e.g. The year 2000:
2000 ÷ 4 = 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000 ÷ 400 = 5 (Leap!)
So the year 2000 is a leap year.

But the year 2100 is not a leap year because:
2100 ÷ 4 = 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)

Warning your output should match the Example Output format exactly, including spelling an punctuation.

Example Input 1
2400
Example Output 1
Leap year

Example Input 2
1989
Example Output 2
Not leap year
'''

year = int(input("Which year do you want to check for Leap year? : "))

if year % 4 == 0:
    if year % 100 ==0: #Not a leap year, unless a special case
        if year % 400 ==0:
            print("Leap year")    
        else:
            print("Not leap year")
    else:
        print("Leap year")    
else:
    print("Not leap year")




## Code Example : Nested If/elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill =5
        print("Child tickets are $5.")        
    elif age <=18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo =="Y":                
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")



## Task 4 - PIZZA ORDER PRACTICE
'''
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1

Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.
'''

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ") 
add_pepperoni = input("Do you want pepperoni? Y or N :") 
extra_cheese = input("Do you want extra cheese? Y or N : ") 

bill = 0

if size == "L":
    bill = 25

elif size == "M":
    bill = 20

else:
    bill = 15


if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

print(f"Your final bill is: ${bill}.")


## Code Example : Logical Operator

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill =5
        print("Child tickets are $5.")        
    elif age <=18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >=45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo =="Y":                
        bill += 3

    print(f"Your final bill is {bill}")    
else:
    print("Sorry, you have to grow taller before you can ride.")



## Task 5 - LOVE CALCULATOR
'''
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3

Love Score = 53

Print: "Your score is 53."

These functions will help you:
lower() count()

Example Input 1
    Kanye West
    Kim Kardashian

Example Output 1
    The Love Calculator is calculating your score...
    Your score is 42, you are alright together.

Example Input 2
    Brad Pitt
    Jennifer Aniston
Example Output 2
    The Love Calculator is calculating your score...
    Your score is 73.

Hint
    You can check your values against mine using this table:

Name 1	            Name 2	            Score
Brad Pitt	        Jennifer Aniston	73
Prince William	    Kate Middleton	    67
Ashton Kutcher	    Mila Kunis	        63
Angela Yu	        Jack Bauer	        53
David Beckham	    Victoria Beckham	45
Kanye West	        Kim Kardashian	    42

'''

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")  
name2 = input("What is your partner name? ") 

# Write your code below this line 👇
combined_names = name1 + name2
lowercase_name = combined_names.lower()

t = lowercase_name.count("t")
r = lowercase_name.count("r")
u = lowercase_name.count("u")
e = lowercase_name.count("e")

first_digit = t + r + u + e

l = lowercase_name.count("l")
o = lowercase_name.count("o")
v = lowercase_name.count("v")
e = lowercase_name.count("e")

second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))

if (love_score<10 or love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score>=40 and love_score<=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")



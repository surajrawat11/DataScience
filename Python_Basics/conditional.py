# IF else

a = 9

if a<4:
    print("a smaller than 4")

else:
    print("a is greater than 4")


money = int(input("Please give money :"))

if money == 10:
    print("I will have alu samosa")

else:
    print("I will have panner samosa")


age = int(input("Enter your age: "))

if age >=21:
    print("Eligible to drink")
elif age>=18:
    print("Eligible to vote")
else:
    print("Under age")


# Accept two numbers and print the greatest between them.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1>num2:
    print(f"{num1} will be greater than {num2}")
elif num2>num1:
    print(f"{num2} will be greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")

# Question 2
"""
Accept the gender from the user as char and print the
respective greeting message
Ex - Good Morning Sir (on the basis of gender)
"""
gen = input("Please tell your gender as character (M or F): ")
if gen == "M" or gen=="m":
    print("Good morning SIR")
elif gen =="F" or gen == "f":
    print("Good morning MAM")
else:
    print("Unidentified gender")

# Question 3

"""
Accept an integer and check whether it is an even number
or odd.
"""

num = int(input("Please give a number : "))
if num%2==0:
    print("given no. is even: ")
else:
    print("given no. is odd")

# Question 4
"""
Accept name and age from the user. Check if the user is a
valid voter or not.
Ex- “hello shery you are a valid voter”
"""    
name = input("Tell your name: ")
age = int(input("Please enter your age: "))

if age>=18:
    print(f"hello {name} you are a valid voter")
else:
    print(f"hello {name} you are not a valid voter")

# Question 5
"""
Accept a year and check if it a leap year or not (google to
find out what is a leap year)
"""

year = int(input("please enter an year :- "))
if year%100 == 0 and year%400 == 0:
    print("It's an leap year: ")
elif year%100 != 0 and year%4 == 0:
    print("It' an leap year: ")
else:
    print("It's an normal year")

# If - elif lader
# used for multiple conditions

"""
Below 0°C → "Freezing Cold" 
0°C to 10°C → "Very Cold"
10°C to 20°C → "Cold"
20°C to 30°C → "Pleasant"
30°C to 40°C → "Hot"
Above 40°C → "Very Hot"
"""

temp = int(input("Please tell the temperature :-"))
if temp<0:
    print("Freezing cold")
elif temp>0 and temp<10:
    print("Very cold")
elif temp>10 and temp<20:
    print("Cold")
elif temp>20 and temp<30:
    print("Pleasant")
elif temp>30 and temp<40:
    print("Hot")
else:
    print("Very hot")


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
    print("Eligible to vote")
elif age>=18:
    print("Eligible to drink")
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
# for loop


for i in range(2,21,2):
    print(i)

n = int(input("enter a number :- "))
for i in range(n,(n*10)+1,n):
    print(i)

a = "SURAJ RAWAT"
for i in range(11):
    print(a[i])

b = "Hello how are you what going on"
for i in range(len(b)):
    print(b[i])

for i in range(1,21):
    if i == 15:
        break
    print(i)

for i in range(1,26):
    if i == 5:
        continue
    print(i) 

# Quetion 1 
# Accept an integer and Print hello world n times

n = int(input("Enter a number :- "))
for i in range(n):
    print("Hello")

# Question 2
# Print natural number up to n
num = int(input("enter a number :- "))
for i in range(1,num+1):
    print(i)

# Question 3
# Reverse for loop. Print n to 1
num = int(input("Enter a number :- "))
for i in range(num,0,-1):
    print(i)

# Question 4
# Take a number as input and print its table
num = int(input("enter a number :- "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}") 

# Question 5
# Sum up to n terms

n = int(input("enter a number :- "))
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(f"The sum is {sum}")

# Question 6
# Factorial of a number

n = int(input("enter a number :- "))
factorial = 1
for i in range(1,n+1):
    factorial = factorial*i
print(f"The factorial of {n} is {factorial}")

# Question 7
# Print the sum of all even & odd numbers in a range separately

n = int(input("enter a number :- "))
even = 0
odd = 0
for i in range(1,n+1):
    if i%2 == 0:
        even = even+i
    else:
        odd = odd+i
print(f"Your even and odd sum are {even} {odd}")

# Question 8
# Print all the factors of a number
n = int(input("enter a number :- "))
for i in range(1,n+1):
    if n%i == 0:
        print(i)

# Question 9
# Accept a number and check if it a perfect number or not.
# A number whose sum of factors is equal to the number itself
# Ex - 6 = 1, 2, 3 = 6

n = int(input("enter a number :- "))
sum = 0
for i in range(1,n):
    if n%i==0:
        sum = sum+i

if sum==n:
    print(f"{n} is an perfect number")
else:
    print(f"{n} is not a perfect number")

# Question 10 
# Check wether the number is prime or not

n = int(input("enter a number :- "))
count = 0

for i in range(1,n+1):
    if n%i==0:
        count = count+1

if count == 2:
    print(f"{n} is a prime number: ")
else:
    print(f"{n} is not a prime number: ")
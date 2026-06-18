a = 1
while a<=30:
    print(a)
    a = a+1

# Question 1
# Separate each digit of a number and print it on the new line.
a = int(input("Tell a number :- "))
while a > 0:
    print(a%10)
    a = a//10

# Question 2
#  Accept a number and print its reverse
b = int(input("enter a number :- "))
rev = 0
while b>0:
    rev = rev*10+b%10
    b = b//10

print(rev)

# Question 3
# Accept a number and check if it is a pallindromic number 
# (If number and its reverse are equal)

c = int(input("Enter a number :- "))
rev = 0
copy = c
while a>0:
    rev = rev*10 + a%10
    c = c//10

if copy==rev:
    print("pallindrome number")
else:
    print("not pallindrome") 
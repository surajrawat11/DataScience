# Question 1
# Reverse a string without using in build functions.
a = "abhimanyu"
print(a[::-1])

b = "prashant kumar"
for i in range(len(b)-1,-1,-1):
    print(b[i])
    

# Question 2
# Check string is Pallindrome or not 

c = "shreyain"
d =""
for i in range(len(c)-1,-1,-1):
    d = d+c[i]

if d == c:
    print("This string is pallindrome")
else:
    print("It's not a pallindrome")

# Question 3 
"""
Count all letters, digits, and special symbols from a given
string

 Given: str1 = "P@#yn26at^&i5ve"

 Expected Outcome:

 Total counts of chars, digits, and symbols

 Chars = 8

 Digits = 3

 Symbol = 4

"""


x = "dldjalkj123326%^&*@#@#"
char = 0
dig = 0
spchr = 0

for i in x:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spchar+=1

print(f"your digit are {dig}\n")
print(f"your characters are {char}\n")
print(f"your special characters are {spchr}\n")



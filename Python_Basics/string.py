# Question 1
# Reverse a string without using in build functions.
a = "abhimanyu"
print(a[::-1])

b = "prashant kumar"
for i in range(len(b)-1,-1,-1):
    print(b[i])
    

# Question 2
# Check string is Pallindrome or not 

c = "Naman"
d =""
for i in range(len(a)-1,-1,-1):
    d = d+c[i]

if d == a:
    print("This string is pallindrome")
else:
    print("It's not a pallindrome")


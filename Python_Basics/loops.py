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

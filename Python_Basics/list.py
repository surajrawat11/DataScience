a = [12,13,14,15,16,34.5,True,print()]
print(a[0:5])

# using index
for i in range(len(a)):
    print(a[i])

# using directly for values

for i in a:
    print(i)

# append

l = [1,2,3,4,5]
l.append(6)
l.append(7)
print(l)

# insert

x = [1,3,4,5]
x.insert(1,2)
print(x)

# remove
# remove first occurence of number
y = [1,2,4,6,2,5,2]
y.remove(2)
print(y)

l = [1,2,3,1,2,4,6]
l[0] = 10
print(l)

# Question 1
#  Print positive and negative elements of an List.
p = [1,-3,2,4,-6,3,-8,9]
print("Postive elements are :- ")
for i in p:
    if i >= 0:
        print(i)
print("Negative elements are :- ")
for i in p:
    if i < 0:
        print(i)

# Question 2
# Mean of List elements.
q = [2,4,5,12,35,13,2,56,59]
sum = 0
for i in q:
    sum = sum + i

print(sum/len(l))

# Question 3
# Find the greatest element and print its index too.
r = [13,236,6346,4213,234,324,64,35,24,36,57,57,86,35,424,4546,7,353]
largest = r[0]
index = 0
for i in range(len(r)):
    if r[i] > largest:
        largest = r[i]
        index = i
print(f"your largest number is {largest} at index {index}")

# Question 4
#  Find the second greatest element.

s = [21,124,32,1,3,2,3,43,54,6,85,345,24,35,46,42,3,57,43,63,67]
largest = l[0]
second_largest = l[0]
index_1 = 0
index_2 = 0
for i in s:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest:
        second_largest = i

print(second_largest,largest)

# Question 5
#  Check if List is sorted or not.

e = [1,3,4,5,6,78,87,90,91,92]

for i in range(len(e)-1):
    if e[i] < e[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("List is sorted")






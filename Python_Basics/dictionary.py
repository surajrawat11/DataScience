a = {}
print(type(a))
# Dictionary has keys and values

d = {1:"hello",2:7}
# Accessing through keys
x = {10:100,20:200,30:300,40:400}
print(x[10])
# we can update the values
x[10] = 1000
print(x)
# updating
x.update({50:500})
print(x)
# deleting
del x[30]
print(x)
for i in x:
    print(x[i])

# Dictionary methods

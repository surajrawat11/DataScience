a = {1,2,3,4,3,5,4}
print(a)

# set as no index value

# Hash values
b = hash("Hello")
print(b)
c = hash((1,32,53,46))
print(c)

# set traversing
"""
A set cannot be traversed using the index values cause it is
unordered and has no index
So many times it will give random values. you can watch the
video for complete understanding.
"""
# set methods
x = {1,4,2,5,3}
x.add(6)
print(x)
x.remove(2)
print(x)
x.pop()
print(x)
x.clear()
print(x)

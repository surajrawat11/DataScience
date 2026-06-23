p = open(r"C:\Users\user\Desktop\DataScience\Python_Basics\list.py")
print(p.read())

# File handling

"""
Mode                Description

'r'    -    Read (default) file must exist.    

'w'    -    Write - creates file or overwrites.

'a'    -    Append - adds to end of file.

'x'    -    Create - creates a new file, fails if it exist
"""

r = open("superman.txt",'a')
r.write("I am appending something")
r.close()


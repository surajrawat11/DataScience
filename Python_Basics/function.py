def hello():
    print("This is a hello function")

hello()

def sum(a,b):
    print(f"The sum of the number is {a+b} ")

sum(6,7)
sum(8,9)
sum(6,1)
sum(7,3)

def hi(name,age):
    print(f"your name is {name} and your age is {age}")

hi("suraj",19)



# check if an string is an pallindrome

def pallindrome(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev = rev+str[i]

    if rev == str:
        print("pallindrome")
    else:
        print("Not a pallindrome")

pallindrome("naman")
pallindrome("suresh")
pallindrome("akash")
pallindrome("racecar")

# return

def greeting():
    return "how are you"

print(greeting())



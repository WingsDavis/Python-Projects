name = input("Enter Your Name: ")
print("Hello", name , "\n")



import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

all = lower + upper
length = 8
password = "".join(random.sample(all,length))

print("This is your generated password")
print(password ,"\n")



numbers = "0123456789"
symbols = "[]{}()*;:/,.?-_"

auth = numbers + symbols
length = 6
verify = "".join(random.sample(auth,length))

print("This is your Verification code")
print(verify , "\n")

print("press y to exit and n to do again")
a = "y"
b = input("Are you ok with it:  ")

if a == b:
    exit()
else:
    print("")

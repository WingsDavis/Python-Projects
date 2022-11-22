import random
print("Author #Wings_W$")
print("This is a dice simulator")
#initializing the values
a = "a"
print("Press any key to exit")
#While loop because we want it to run until the user wants to exit by pressing any key
while a == "a":
    #where dice is the variable
    #"randint" for random variables
    dice = random.randint(1,6) #with range from 1-6
    #if conditions for the dice to roll
    if dice == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if dice == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if dice == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if dice == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if dice == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if dice == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    a = input("Press a to roll again: ")
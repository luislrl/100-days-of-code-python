from ascii_art import logo
import os

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def multi(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2

def do_next():
    choice = input('You want to keep calculating with the result, or start a new calculation? r/n\nIf you want to leave, type "end"\n')
    
    if choice.lower() == "r":
        return 0
    elif choice.lower() == "n":
        os.system('cls')
        return 1
    elif choice.lower() == "end":
        return 2
    else:
        print("Invalid answer, type again:")
        do_next()

operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div,
}

to_do = 1

while to_do != 2:
    if to_do == 1:
        num1 = float(input("Type the first number\n"))
    else:
        num1 = result    

    print("What operation you want to do?")
    for operation in operations:
        print(operation)
    op = input("(Choose from the symbols above)\n")

    num2 = float(input("Type the second number\n"))

    for key in operations:
        if op == key:
            result =operations[key](num1, num2)
            print(result)

    to_do = do_next()
from art import logo
import os


def calculator(n1, n2):
    if op == "+":
        result = n1 + n2
    elif op == "-":
        result = n1 - n2
    elif op == "*":
        result = n1 * n2
    elif op == "/":
        result = n1 / n2

    return result


keep_running = True
first_ite = True

while keep_running:
    os.system("cls")

    print(logo)

    if first_ite:
        n1 = float(input("What is the first number?: "))
    else:
        n1 = result
        print(f"The first number is = {result}")

    op = input("+\n-\n*\n/\nPick an operation: ")

    n2 = float(input("What is the next number?: "))

    result = calculator(n1, n2)

    print(f"{n1} {op} {n2} = {result}")

    keep_going = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, Type 'e' ito exit: "
    )
    if keep_going == "y":
        first_ite = False
    elif keep_going == "n":
        first_ite = True
        os.system("cls")
        continue
    else:
        keep_running = False

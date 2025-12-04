from art import logo



def add(n1, n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

calculation = {"+": add, "-": substract, "*": multiply, "/": divide,}

def calculator():
    print (logo)
    should_continue = True
    first_number = float(input("what's the first number?: "))
    while should_continue:
        print(f"+\n-\n*\n/")

        operation = input("Pick an Operation: ")

        second_number = float(input("What's the second number?: "))

        answer =calculation[operation](first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation ")

        if choice == "y":
            first_number = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
calculator()
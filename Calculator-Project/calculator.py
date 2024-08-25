import art
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    print (art.logo)
    num1 = float((input("Type the first number: ")))

    should_continue = True

    while should_continue:
        print("operations:")
        for i in operations:
            print('"'+ i +'",', end = " ")
        symbol = input("\npick an operation: ")
        num2 = float((input("Type the second number: ")))
        answer = operations[symbol](num1, num2)
        print(f"The equation is: {num1} {symbol} {num2} = {answer}")

        choice = input(f"type y to continue calculating with {answer} or type n to start new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 5)
            calculator()

calculator()

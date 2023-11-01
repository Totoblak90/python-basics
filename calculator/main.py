# Calculator

def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}


def calculator():

    num1 = float(input("What's the first number?: "))

    [print(operation) for operation in operations]
    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        bla = input(f"Type 'y' to continue calculating with {
                    answer}, or type 'r' to start a new calculation, or type 'q' to quit: ")

        if bla == 'y':
            num1 = answer
        elif bla == 'r':
            should_continue = False
            calculator()
        elif bla == 'q':
            should_continue = False
        else:
            raise ValueError('Invalid selection')


calculator()

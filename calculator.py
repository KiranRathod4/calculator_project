import art
from art import text2art

def add(n1,n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

""" creating a dictionary for operations to save what is key and its value"""
operations  = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}
def calculation():
    print(text2art("CALCULATOR"))

    should_acumlate = True
    num1=float(input("what is the first number:"))
    while should_acumlate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("pick an operation:")
        num2 = float(input("what is next number:"))
        answer = operations[operation_symbol](num1 , num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice  = input(f"type 'y' if you want to continue calculation with {answer} or type 'n' to start new calculation:")
        if choice =="y":
            num1 = answer
        else:
            should_acumlate = False
            print("\n" *20 )
            calculation()

calculation()
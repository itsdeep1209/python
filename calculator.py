# program to write a simple calculator function for add , sub , mult and div

def calculator():
    while True:
        try:
            num1 = float(input("Enter first number:"))
            op = input("Enter operator(+,-,*,/):")
            num2 = float(input("Enter second number:"))
            if op == "+":
                print(num1 + num2)
            elif op == "-":
                print(num1 - num2)
            elif op == "*":
                print(num1 * num2)
            elif op == "/":
                print(num1 / num2)
            else:
                print("invalid operator")
            break
        except ValueError:
            print("Invalid input, try again")

calculator()
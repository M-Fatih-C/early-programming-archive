# -*- coding: utf-8 -*-

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        print("Invalid operator")

while True:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator: ")
    num2 = float(input("Enter the second number: "))

    result = calculator(num1, num2, operator)
    print("The result is: ", result)

    if input("Do you want to continue? (y/n): ") == "n":
        break

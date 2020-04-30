"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



def calculator():
    """Interface for a calculator

    receives a string, breaks it into usable parts, outputs a number"""
    quit = False
    
    while quit is False: 
        math_equation = input("Enter your equation: ").split(" ")

        action = str(math_equation[0])

        if action == "q" or action == "quit":
            break

        elif action == '+':
            num1 = float(math_equation[1])
            num2 = float(math_equation[2])
            print(add(num1, num2))
        elif action == '-':
            num1 = float(math_equation[1])
            num2 = float(math_equation[2])
            print(subtract(num1, num2))
        elif action == '*':
            num1 = float(math_equation[1])
            num2 = float(math_equation[2])
            print(multiply(num1, num2))
        elif action == '/':
            num1 = float(math_equation[1])
            num2 = float(math_equation[2])
            print(divide(num1, num2))
        elif action == 'square':
            num1 = float(math_equation[1])
            print(square(num1))
        elif action == 'cube':
            num1 = float(math_equation[1])
            print(cube(num1))
        elif action == 'pow':
            num1 = float(math_equation[1])
            num2 = float(math_equation[2])
            print(power(num1, num2))
        elif action == 'mod':
            num1 = float(math_equation[1])
            num2 = float(math_equation[2])
            print(mod(num1, num2))
        else:
            action == "q" or action == "quit"
            break

    return "not working"

print(calculator())
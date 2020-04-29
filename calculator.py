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
        num1 = float(math_equation[1])
        num2 = float(math_equation[2])
        #num3 = float(math_equation[3])

        if action == '+':
            print(add(num1, num2))
        elif action == '-':
            print(subtract(num1, num2))
        elif action == '*':
            print(multiply(num1, num2))
        elif action == '/':
            print(divide(num1, num2))
        elif action == 'square':
            print(square(num1))
        elif action == 'cube':
            return num1 * num1 * num1
        elif action == 'power':
            return num1 ** num2
        elif action == 'mod':
            return num1 % num2
        #else action.lower() == "q" or action == "quit":
        #    break

    return "not working"

print(calculator())
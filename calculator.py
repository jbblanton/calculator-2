"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

math_equation = input("Enter your equation: ").split(" ")

def calculator(function, *num):
    """Interface for a calculator

    receives a string, breaks it into usable parts, outputs a number"""




    return [function, num]

print(calculator(math_equation))
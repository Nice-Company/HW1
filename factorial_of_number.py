"""
This module contains a method for calculating the factorial of a number.
"""

def factorial(num1):
    """
    A method to get the factorial of a number.
    """
    if num1 <= 1:
        return 1
    return factorial(num1 - 1) * num1


NUM = 5

fact = factorial(NUM)

print("factorial of 5:", fact)

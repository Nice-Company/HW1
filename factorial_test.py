"""
This module contains tests for factorial_of_number.py
"""

from factorial_of_number import factorial


def test_factorial_of_five():
    """
    Testing the value of factorial for number 5.
    """
    assert factorial(5) == 120


def test_factorial_of_four():
    """
    Testing the value of factorial for number 10.
    """
    assert factorial(4) == 24

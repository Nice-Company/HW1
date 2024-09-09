"""
Test file to test the merge sort code.
"""
from hw2_debugging import merge_sort


def test_no_elements():
    """
    Test case for sorting no elements
    """
    assert merge_sort([]) == []


def test_one_element():
    """
    Test case for sorting one element
    """
    assert merge_sort([3]) == [3]


def test_five_elements():
    """
    Test case for sorting five elements
    """
    assert merge_sort([6, 3, 20, 5, 2]) == [2, 3, 6, 20]

def test_eight_elements():
    """
    Test case for sorting eight elements. It is deliberately kept failing.
    """
    assert merge_sort([8, 3, 9, 10, 3, 6, 1, 2]) == [1, 2, 3, 3, 6, 8, 9, 10]
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
    assert merge_sort([6, 3, 20, 5, 2]) == [2, 3, 5, 6, 20]

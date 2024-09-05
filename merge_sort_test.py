from hw2_debugging import mergeSort

def test_no_elements():
    assert mergeSort([]) == []

def test_one_element():
    assert mergeSort([3]) == [3]

def test_five_elements():
    assert mergeSort([6,3,20,5,2]) == [2,3,5,6,20]                     
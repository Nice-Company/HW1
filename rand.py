"""
This class generates random numbers in an array
"""
import subprocess


def random_array(arr):
    """
    Generates an array with random integers.
    Args:
        arr (list): the list to be generated.
    Returns:
        list: an array with a list of random numbers.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout.strip())
    return arr

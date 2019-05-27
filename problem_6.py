"""
Project 3: Problems vs Algorithms
Problem 6. Max and Min in a Unsorted Array

  We look for smallest and largest integer from a list of unsorted integers.
  
  Time: O(n), where n is the input size. It scans the array of int once.
  Space: O(1)

"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == None:
        return (None, None)
    n = len(ints)
    if n == 0:
        return (None, None)
    if n == 1:
        return (ints[0], ints[0])
    dmin = ints[0]
    dmax = ints[0]
    for k in range(1,n):
        d = ints[k]
        if dmin > d:
            dmin = d
        if dmax < d:
            dmax = d
    return (dmin, dmax)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
l = [7, 6, 8]
print("Pass" if ((6, 8) == get_min_max(l)) else "Fail")

print("Pass" if ((None, None) == get_min_max(None)) else "Fail")
print("Pass" if ((None, None) == get_min_max([])) else "Fail")

print("Pass" if ((14, 14) == get_min_max([14])) else "Fail")
l = [i for i in range(0, 100)]  # a list containing 0 - 99
random.shuffle(l)
print("Pass" if ((0, 99) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)
print("Pass" if ((0, 999) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 1000000)]  # a list containing 0 - 999999
print("Pass" if ((0, 999999) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 10000000)]  # a list containing 0 - 9999999
print("Pass" if ((0, 9999999) == get_min_max(l)) else "Fail")

"""
Output:

Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
"""

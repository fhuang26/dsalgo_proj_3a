"""
Project 3: Problems vs Algorithms
Problem 2. Search in a Rotated Sorted Array

Given a sorted array which is rotated at some random pivot point,
e.g., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2], and
we want to know whether a target number is in the input array.

We do a binary search (bs1) to look for the rotation boundary.
Then with rotation boundary, we do binary search (bs2) on two increasing
sections to check for target.

Time: O(log n), where n is the input size. Two or three binary searches
                take O(log n) time.
Space: O(1)

"""
def bs1(a, l, h):
    """
      binary search to look for a[k] > a[k+1], rotation boundary
         a: int array
         l: low index
         h: high index
      returns k
      or returns -1: no such k (whole array a is sorted)
    """
    #print((a, l, h))
    if l > h:
        return -1
    if l == h:
        if h+1 < len(a) and a[h] > a[h+1]:
            return h
        else:
            return -1
    m = (l + h)//2  # middle
    if m+1 < len(a) and a[m] > a[m+1]:
        return m
    if a[m] > a[h]:
        return bs1(a, m+1, h)
    return bs1(a, l, m) # m is used to keep the boundary inside the left half.

def bs2(a, l, h, target):
    if l > h:
        return -1
    if l == h:
        if a[h] == target:
            return h
        else:
            return -1
    m = (l + h)//2  # middle
    if a[m] == target:
        return m
    if a[m] < target:
        return bs2(a, m+1, h, target)
    return bs2(a, l, m-1, target)
    
def rotated_array_search(a, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       a(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    n = len(a)
    k = bs1(a, 0, n-1)
    
    if k == -1: # array a is sorted
        return bs2(a, 0, n-1, number)
    j = bs2(a, 0, k, number)
    if j >= 0:
        return j
    return bs2(a, k+1, n-1, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 5], 4])
test_function([[1, 2, 3, 4, 5], 1])
test_function([[1, 2, 3, 4, 5], 3])
test_function([[1, 2, 3, 4, 5], 6])
test_function([[8, 1, 2, 3, 4, 5, 6, 7], 8])
test_function([[8, 1, 2, 3, 4, 5, 6, 7], 1])
test_function([[8, 1, 2, 3, 4, 5, 6, 7], 9])
test_function([[8, 1, 2, 3, 4, 5, 6, 7], 5])

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
Pass
Pass
Pass
Pass
Pass

"""

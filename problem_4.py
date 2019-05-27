"""
Project 3: Problems vs Algorithms
Problem 4. Dutch National Flag

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

We maintain 3 indices: l, m, r for 0s, 1s, 2s respectively. Initially l=0, m=0,
and r = n-1, where n is the input size. While m <= r, check d = a[m] and do
the following.

(1) If d is 0, swap a[l] and a[m], increment l, and increment m.

(2) If d is 1, increment m.

(3) If d is 2, swap a[m] and a[r], decrement r.

Resulting array is sorted.

Time: O(n), where n is the input size. It scans the array once and does swap as
       needed.
Space: O(1)
"""
def sort_012(a):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       a(list): List to be sorted
    """
    if a == None:
        return None
    
    n = len(a)
    if n <= 1:
        return a
    
    l = 0 # left index for 0s
    m = 0 # middle index for 1s
    r = n-1 # right index for 2s
    while m <= r:
        d = a[m]
        if d == 0:
            tmp = a[l]
            a[l] = a[m]
            a[m] = tmp
            l += 1
            m += 1
        elif d == 1:
            m += 1
        else: # d == 2
            tmp = a[m]
            a[m] = a[r]
            a[r] = tmp
            r -= 1
    return a

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0])
test_function([1, 1])
test_function([2, 2, 2])
test_function([])
test_function([0, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1, 2, 0])
test_function([1, 1, 2, 1, 0, 2, 2, 0, 1, 0, 0, 2, 2, 2, 1, 2, 1, 0, 0, 0, 1, 0, 2, 1, 0, 1, 2, 0])
test_function([2, 2, 2, 2, 0, 2, 0, 1, 1, 0, 0, 2, 2, 2, 1, 0, 2, 0, 1, 1, 2, 0, 2, 2, 1, 1, 2, 0])
test_function([0, 2, 0, 0, 0, 2, 1, 1, 1, 0, 0, 2, 0, 2, 1, 0, 0, 0, 1, 2, 2, 0, 0, 0, 1, 1, 2])
test_function([1, 0, 0, 1, 0, 2, 2, 2, 1, 0, 0, 2, 0, 2, 1, 1, 1, 0, 2, 0, 0, 0, 0, 1, 2, 1, 2])
test_function([2, 0, 0, 2, 0, 2, 0, 2, 1, 0, 0, 2, 0, 2, 1, 1, 2, 0, 2, 1, 0, 0, 0, 2, 2, 1, 2])
test_function([0, 1, 1, 0, 0, 2, 1, 0, 1, 0, 0, 2, 1, 2, 1, 2, 0, 0, 0, 2, 1, 0, 1, 0, 0, 1])
test_function([1, 1, 1, 1, 0, 2, 2, 0, 1, 0, 0, 2, 1, 2, 1, 2, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1])
test_function([2, 2, 1, 2, 0, 2, 0, 1, 1, 0, 0, 2, 1, 2, 1, 0, 2, 0, 1, 1, 2, 0, 1, 2, 1, 1])

"""
Output:

[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0]
Pass
[1, 1]
Pass
[2, 2, 2]
Pass
[]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass

"""
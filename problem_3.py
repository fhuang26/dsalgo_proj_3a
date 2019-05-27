"""
Project 3: Problems vs Algorithms
Problem 3. Rearrange Array Elements

Given an array of digits 0, 1, ..., 9, we try to form two number such that
their sum is maximum. The number of digits in both the numbers cannot differ
by more than 1.

For example, input a = [1, 2, 3, 4, 5].
The expected answer would be [531, 42]. Another expected answer can be [542, 31].

We do counting sort as follows.

(1) We count frequency of digits. This takes O(n) time, where n is the input size,
    and O(1) space.

(2) Based on their frequencies, we go through digits from 0 to 9 to form two numbers
    from unit place, 10's place, 100's place,to higher places. This takes O(n) time
    and O(1) space.

This approach can handle duplicate digits.


Time: O(n), where n is the input size. Both (1) and (2) takes O(n) time.
Space: O(1)

"""

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List of digits
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list == None:
        return [None, None]
    n = len(input_list)
    if n <= 1:
        return [None, None]
    if n == 2:
        x = input_list[0]
        y = input_list[1]
        return [min(x,y), max(x,y)]
    
    freq = [0] * 10 # frequency of digits
    for d in input_list:
        freq[d] += 1
    
    base = 1
    x = 0 # the smaller of two numbers
    y = 0 # the bigger of two numbers
    k = 0 # kth digit from small to big
    for d in range(0, 10): # d is a digit
        f = freq[d]
        if f == 0:
            continue
        for j in range(f):
            if k > 0 and k%2 == 0:
                base = 10 * base
            d2 = d * base
            if k == n-1:  # the last big digit is added the larger y
                y += d2   # y: larger
            else:
                if k%2 == 0:
                    x += d2  # x: smaller
                else:
                    y += d2  # y: larger
            k += 1
        if k == n:
            break
    result = [y,x]
    #print(result)
    return result

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if solution == [None, None]:
        if output == solution:
            print("Pass")
        else:
            print("Fail")
        return
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], [None, None]])
test_function([[7,6,8,7,2,3,1,3], [8732,7631]])  # duplicate digits are allowed
test_function([[7,6,8,7,2,3,1], [8762,731]])     # duplicate digits are allowed

"""
Output:

Pass
Pass
Pass
Pass
Pass

"""

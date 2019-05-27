"""
Project 3: Problems vs Algorithms
Problem 1. Square root of int

  For input int n >= 0, we do binary search to look for x such that
    x^2 <= n and (x+1)^2 > n .
  Then x is the floored square root of n.
  
  Time: O(log n)
  Space: O(1)

"""
def binary_search(n, l, h):
    if l > h:
        return -1
    if l == h:
        p = l*l
        q = (l+1)*(l+1)
        if p <= n and q > n:
            return l
    
    m = (l + h)//2  # middle
    p = m*m
    if p <= n:
        q = (m+1)*(m+1)
        if q > n:
            return m
        else:
            # q <= n
            return binary_search(n,m+1,h)
    # p > n:
    return binary_search(n,l,m-1)

def sqrt(n):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # We do binary search
    d = binary_search(n, 0, n)
    return d

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (6 == sqrt(39)) else "Fail")
print ("Pass" if  (7 == sqrt(49)) else "Fail")
print ("Pass" if  (8 == sqrt(78)) else "Fail")
print ("Pass" if  (None == sqrt(-2)) else "Fail")
print ("Pass" if  (9 == sqrt(82)) else "Fail")
print ("Pass" if  (9 == sqrt(94)) else "Fail")
print ("Pass" if  (7 == sqrt(62)) else "Fail")
print ("Pass" if  (45 == sqrt(2028)) else "Fail")
print ("Pass" if  (1000 == sqrt(1000000)) else "Fail")

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
Pass

"""
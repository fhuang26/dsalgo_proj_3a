## Project 3: Problems vs Algorithms
### Problem 1. Square root of int

  For input int n >= 0, we do binary search to look for x such that
    x^2 <= n and (x+1)^2 > n .
  Then x is the floored square root of n.
  
* Time: O(log n)
* Space: O(1)

### Problem 2. Search in a Rotated Sorted Array

Given a sorted array which is rotated at some random pivot point,
e.g., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2], and
we want to know whether a target number is in the input array.

We do a binary search (bs1) to look for the rotation boundary.
Then with rotation boundary, we do binary search (bs2) on two increasing
sections to check for target.

* Time: O(log n), where n is the input size. Two or three binary searches
                take O(log n) time.
* Space: O(1)

### Problem 3. Rearrange Array Elements

Given an array of digits 0, 1, ..., 9, we try to form two number such that
their sum is maximum. The number of digits in both the numbers cannot differ
by more than 1.

For example, input a = [1, 2, 3, 4, 5].
The expected answer would be [531, 42]. Another expected answer can be [542, 31].

We do counting sort as follows.

(1) We count frequency of digits. This takes O(n) time, where n is the input size,
    and O(1) space.

(2) Based on frequency of digits, we go through digits from 0 to 9 to form two numbers
    from unit place, 10's place, 100's place, to higher places. This takes O(n) time
    and O(1) space.

This approach can handle duplicate digits.

* Time: O(n), where n is the input size. Both (1) and (2) takes O(n) time.
* Space: O(1)


### Problem 4. Dutch National Flag

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

We maintain 3 indices: l, m, r for 0s, 1s, 2s respectively. Initially l=0, m=0,
and r = n-1, where n is the input size. While m <= r, check d = a[m] and do
the following.

* If d is 0, swap a[l] and a[m], increment l, and increment m.

* If d is 1, increment m.

* If d is 2, swap a[m] and a[r], decrement r.

Resulting array is sorted. It visits every element of the array once and does
necessary swaps.

* Time: O(n), where n is the input size.
* Space: O(1)

### Problem 5. Autocomplete with Tries

We build the trie from a set of words, and then support autocompletion
by using the trie and suffix calucation.

* suffixes() in TrieNode class takes O(n) time, where n is the number of nodes
in the subtree. It takes O(n) space for the number of nodes and suffixes in
the subtree.

* insert() in Trie class takes O(n) time, where n is the word length. It takes
O(n) space for nodes of chars in the word.

* find() in Trie class takes O(n) time, where n is the word length, and
O(1) space.

### Problem 6. Max and Min in a Unsorted Array

  We look for smallest and largest integer from a list of unsorted integers.
  
* Time: O(n), where n is the input size. It scans the array of int once.
* Space: O(1)

### Problem 7. HTTP Router using a Trie

In addition to a path though, we need to know which function will handle the http request. we will just use a string that we can print out to ensure we got the right handler.

A Trie with a single path entry of: "/about/me" would look like:
   (root, None) -> ("about", None) -> ("me", "about me handler")
   
* insert() in RouteTrie class takes O(n) time, where n is the size of path, and
        O(1) space.

* find() in RouteTrie class takes O(n) time, where n is the size of path, and
        O(1) space.

* add_handler() in Route class takes O(n) time, where n is the length of input
path. It takes O(n) space for a list of tokens along the path.

* lookup() in Route class takes O(n) time, where n is the length of input path.
It takes O(n) space for a list of tokens along the path.

# Section 14: Algorithms: Searching + BFS + DFS

### Linear Search

Loop through the items one-by-one and check if they match the target value. $O(n)$ time complexity.

### Binary Search

Useful if data is sorted. Time complexity is $O(n\log{n})$.

A sorted array is the same as a binary search tree!
```py
[1, 4, 5, 8, 9, 10, 13]
```
```
     8
   /   \
  4    10
 / \   / \
1   5 9  13
```

Split the numbers in half, compare the values to the left. If they're less than what we're looking for, throw away the left side of the list. Repeat the process with the right side, until the mid-point marker ends up being our target value.

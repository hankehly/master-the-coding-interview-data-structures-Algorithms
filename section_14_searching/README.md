# Section 14: Algorithms: Searching + BFS + DFS

## Algorithms

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

### Breadth First Search (BFS)

(See section_10_trees for implementation)

* We traverse the nodes from top to bottom, left to right (picture a curtain coming down at the end of a play, or reading a book)
* $O(n)$ time complexity
* Uses more memory than DFS because we need to keep track of many pointers
* Good for finding the shortest path between nodes
* If you know the target node is in the upper level of a tree, use BFS.

```
     8
   /   \
  4    10
 / \   / \
1   5 9  13
```
```py
[8, 4, 10, 1, 5, 9, 13]
```

### Depth First Search (DFS)

* We go as deep as we can to the left, then once we run out of nodes, start going to the right.
* $O(n)$ time complexity
* Uses less memory than BFS, but can be slower
* Good for asking the question "does the node exist?"

```
     8
   /   \
  4    10
 / \   / \
1   5 9  13
```
```py
[8, 4, 1, 5, 10, 9, 13]
```

## When to use BFS/DFS

**If you know a solution is not far from the root of the tree:**

BFS, because you always start searching from the root node.

**If the tree is very deep and solutions are rare:**

You'd want to use BFS here, because DFS is gonna take a long time going up and down. However, BFS uses more memory, so if you're concerned about space, DFS might be more appropriate (but probably slower).

**If the tree is very wide:**

You want to use DFS here, because of space complexity. Really wide trees will consume a ton of memory if using BFS.

**If solutions are frequent but located deep in the tree:**

DFS, because we want to check deep nodes first.

**Determining whether a path exists between two nodes:**

DFS, because the nodes may be distant in tree height.

**Finding the shortest path:**

BFS, because going from top to bottom will tell us first the shortest path between the two target nodes.

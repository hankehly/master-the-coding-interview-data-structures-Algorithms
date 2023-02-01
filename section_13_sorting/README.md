# Section 13: Algorithms: Sorting

* Learning sorting is important for working with large inputs, when we can't just rely on builtin `sort` functions from the programming language.
* Depending on how the data is sorted (random, reversed, nearly sorted, etc..) different algorithms will perform better.

## Algorithms

### Bubble Sort

Time complexity is $O(n^2)$, space complexity is $O(1)$. Pretty bad..

You make repeated trips through the array from left to right and *bubble up* the higher number in the current 2-item window.

On each trip, bubble-sort guarantees that the highest number in the list gets *bubbled up* to the last position. Therefore, we only need to make `len(array)` trips through the list to guarantee that it gets completely sorted.

You could optimize the algorithm by using a while loop and checking on each iteration whether the last run made a swap or not. If it didn't, you can exit early!

```py
# Start:
[2, 7, 5, 1, 4]

# [2, 7] are the first pair. 2 < 7 is True, so no need to do anything.
[2, 7, 5, 1, 4]

# [7, 5] are the next pair. 7 < 5 is False, so swap their places
[2, 5, 7, 1, 4]

# [7, 1] are the next pair. 7 < 1 is False, so swap their places
[2, 5, 1, 7, 4]
```

### Selection Sort

Repeatedly scan the list (like bubble sort) and each time, find the smallest item. Move it to first place and repeat. The second time around, move the smallest item to the second place, and so forth..

Also bad time complexity $O(n^2)$, space complexity same as bubble sort $O(1)$.

### Insertion Sort

You step through the array and on each iteration, you pause and consider the items before it, in order (ie. backwards). If the item before it is bigger, swap. Repeat this process of swapping until the previous item is smaller than the current item. Then, you move on to the next item in the list (the outer loop).

If the data is nearly sorted, you want to use insertion sort. Best time complexity is near $O(n)$.

### Merge Sort

Divide and conquer strategy. Divide the array into two parts (left, right) and submit to "merge" function. The key is to use recursion to divide the initial array into left/right split until both are single-item lists, then build the array back up using the merge function, which combines the elements in both arrays in sorted order.

See the function docstring for details.

Time complexity is $O(n\log{n})$ but space complexity is $O(n)$, so it uses more space than bubble, selection or insertion sort.

Merge sort is *stable*, so items with the same value appear in the same order in the output.

### Quick Sort

On average (one of) the best sorting algorithm in terms of time ($O(n\log{n})$) and space ($O(n\log{n})$) complexity. However, depending on the chosen "pivot" point, the time complexity can get really bad (worst case is $O(n^2)$).

Quick sort is *unstable*, so items with the same value may appear in different order in the output.

### Heap Sort

Quick Sort and Heap Sort are commonly compared.

* https://brilliant.org/wiki/heap-sort/
* [Quicksort vs heapsort](https://stackoverflow.com/questions/2467751/quicksort-vs-heapsort)

### Radix Sort / Counting Sort / Bucket Sort

These are "non comparison" sorting algorithms. They take advantage of the way integers are stored in memory to sort the data. They only work with integers in a certain range, so they aren't as versitile as merge or quick sort. However, their time complexity can on average beat $O(n\log{n})$.

* [Radix Sort](https://brilliant.org/wiki/radix-sort/)
* [Radix Sort Animation](https://www.cs.usfca.edu/~galles/visualization/RadixSort.html)
* [Counting Sort](https://brilliant.org/wiki/counting-sort/)
* [Counting Sort Animation](https://www.cs.usfca.edu/~galles/visualization/CountingSort.html)

### Timsort

Python's `sorted` builtin function uses this algorithm. It's a combination of merge & insertion sort.


## When to use what?

| Algorithm      | When to use                                                                                                                                                                            |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bubble Sort    | Never (just a teaching mechanism)                                                                                                                                                      |
| Selection Sort | Never (just a teaching mechanism)                                                                                                                                                      |
| Insertion Sort | Only a few items, mostly sorted (can beat $O(n\log{n})$)                                                                                                                               |
| Merge Sort     | When you're worried about worst case and need to guarantee $O(n\log{n})$ time complexity. Space complexity is $O(n)$ so don't use it you're worried about saving memory.               |
| Quick Sort     | When you're worried about saving memory. Quick Sort has better space complexity than merge sort. Only downside is that bad choice of pivot results in $O(n^2)$ time complexity. |

### Example interview problems

**1. Sort 10 schools around your house by distance:**

Use insertion sort for small number of inputs like this.

**2. eBay sorts listings by the current Bid amount:**

Use radix or counting sort, becasue we are sorting numbers in a small range (bids probably don't exceed thousands of dollars..)

**3. Sport scores on ESPN**

Quick sort / merge sort. Depends on space/stability constraints.

**4. Massive database (can't fit all into memory) needs to sort through past year's user data**

If we're concerned about the worst case and we use external sorting (outside of memory), merge sort is the better option.

If we're doing this in memory (for some reason), you might use quick sort to conserve space.

**5. Almost sorted Udemy review data needs to update and add 2 new reviews**

We could get near $O(n)$ time using insertion sort, because the data is almost sorted.

**6. Temperature Records for the past 50 years in Canada**

If the inputs are integers, consider using a non-comparison algorithm like radix or counting sort.

If the inputs are floats, use quick sort to save space because this is a large number of inputs.

**7. Large user name database needs to be sorted. Data is very random.**

Use quicksort for cases like this when inputs are large and the order of same inputs does not matter.

**8. You want to teach sorting for the first time**

Teach bubble sort or selection sort.

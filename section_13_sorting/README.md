# Section 13: Algorithms: Sorting

* Learning sorting is important for working with large inputs, when we can't just rely on builtin `sort` functions from the programming language.
* Depending on how the data is sorted (random, reversed, nearly sorted, etc..) different algorithms will perform better.

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

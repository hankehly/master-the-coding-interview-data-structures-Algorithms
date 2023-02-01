import logging
import os
from typing import List

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)


def bubble_sort(arr: List[int], inplace: bool = False):
    """
    Refer to README for explanation.
    """
    if not inplace:
        arr = list(arr)
    n = len(arr)
    if n == 1:
        return arr
    for _ in range(n):
        for i in range(n):
            j = i + 1
            if j == n:
                break
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def bubble_sort_optimized(arr: List[int], inplace: bool = False) -> List[int]:
    """
    Optimized bubble_sort that checks if the last run made any updates.
    If not, we exit early.
    """
    if not inplace:
        arr = list(arr)
    n = len(arr)
    if n == 1:
        return arr
    logger = logging.getLogger("bubble_sort_optimized")
    in_progress = True
    n_iter = 0  # just for inspection
    while in_progress:
        in_progress = False
        # print("hello")
        for i in range(n):
            j = i + 1
            if j == n:
                break
            elif arr[i] > arr[j]:
                in_progress = True
                arr[i], arr[j] = arr[j], arr[i]
        n_iter += 1
    logger.debug(f"Made {n_iter} trip(s) through the input list")
    return arr


def selection_sort(arr: List[int], inplace: bool = False) -> List[int]:
    """
    See README for description of how this algorithm works.
    """
    if not inplace:
        arr = list(arr)
    n = len(arr)
    if n == 1:
        return arr
    for i in range(n):
        # Initialize the minimum value index at first position (of remaining unsorted list)
        min_i = i
        # Loop through remaining unsorted list
        for j in range(i, n):
            # Find the min value and store it's index in min_i
            if arr[j] < arr[min_i]:
                min_i = j
        # Move the min value to the first position
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


def insertion_sort(arr: List[int], inplace: bool = False) -> List[int]:
    logger = logging.getLogger("insertion_sort")
    if not inplace:
        arr = list(arr)
    logger.debug(f"start with: {arr}")
    # 1. Consider the items one by one. After each iteration, the item at position `i` will
    #    have been moved to the correct sorted order at the beginning of the list, and only i:n
    #    will be unsorted.
    for i in range(len(arr)):
        logger.debug(f"Alright, looking at index {i} (value {arr[i]})")
        # 2. Go backwards from i. Until you encounter a value less than that of arr[i]
        #    keep swapping it with the element before it.
        for j in range(i - 1, -1, -1):
            logger.debug(f"{arr[j]} > {arr[j+1]} ?")
            # 3. arr[i] might be been swapped already, so we should use arr[j+1] instead
            if arr[j] > arr[j + 1]:
                logger.debug(f"swap {arr[j+1]} with {arr[j]}")
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                logger.debug(f"new arr: {arr}")
            else:
                logger.debug("break")
                break
    return arr


def _merge(left: List[int], right: List[int]) -> List[int]:
    """
    The merge logic of the merge_sort algorithm.
    """
    arr = []
    # The idea here is to continuously pick items off of the left side of each list,
    # in order of lowest to highest.
    # Keep a position marker for each list, then on each iteration compare the values
    # at the appropriate position markers.
    i = j = 0
    # Until we reach the end of one of the lists..
    while i < len(left) and j < len(right):
        # Compare and update the appropriate position marker
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    # At this point, we know either left or right is empty, so add the remaining (sorted)
    # elements to the end of the output list we created. One of these calls is meaningless
    # but we don't know which has items, so just do both.
    arr.extend(left[i:])
    arr.extend(right[j:])
    logging.debug(f"_merge({left}, {right}) => {arr}")
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    if n == 1:
        return arr
    mid_point = n // 2
    logging.debug(f"merge_sort_left({arr[:mid_point]})")
    left = merge_sort(arr[:mid_point])
    logging.debug(f"merge_sort_right({arr[mid_point:]})")
    right = merge_sort(arr[mid_point:])
    return _merge(left, right)


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    expected_output = sorted(numbers)
    assert (
        bubble_sort(numbers)
        == bubble_sort_optimized(numbers)
        == selection_sort(numbers)
        == insertion_sort(numbers)
        == merge_sort(numbers)
        == expected_output
    )

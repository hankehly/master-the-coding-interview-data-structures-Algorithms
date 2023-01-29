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


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    expected_output = sorted(numbers)
    assert (
        bubble_sort(numbers)
        == bubble_sort_optimized(numbers)
        == selection_sort(numbers)
        == expected_output
    )
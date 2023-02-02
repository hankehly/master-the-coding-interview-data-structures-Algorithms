import logging
import os
from typing import Any, List

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)


def linear_search(arr: List[Any], x: Any) -> int:
    """
    A linear search for x in arr.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i


def binary_search(arr: List[int], low: int, high: int, x: int) -> int:
    """
    Instead of recursively calling binary_search on the splitted array (which
    messes up the indices) keep track of where the subset starts and ends.

    The indices get confusing..

    arr: List[int]
        the original array
    low: int
        the index of the first element in the subset
    high: int
        the index of the last element in the subset
    x: int
        the value we are looking for
    """
    if high >= low:
        mid = (low + high) // 2
        logging.debug(
            f"x: {x}, arr[mid]: {arr[mid]}, arr: {arr}, subset: {arr[low:high+1]}, left: {arr[low:mid]}, right: {arr[mid+1:high+1]}, mid: {mid} ({low} + {high} // 2)"
        )
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            # Search the left subset (arr[low:mid])
            # Remember, the 'high' parameter is the last element of the subset we want to include in our search.
            # Setting high=mid-1 here means our next subset will be arr[low:mid], which does not include the current 'mid' value.
            return binary_search(arr, low, mid - 1, x)
        else:
            # Search the right subset.
            return binary_search(arr, mid + 1, high, x)
    return -1


if __name__ == "__main__":
    names = ["Bob", "George", "Sally"]
    assert linear_search(names, "George") == names.index("George") == 1

    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert binary_search(arr, 0, len(arr) - 1, 1) == 0
    assert binary_search(arr, 0, len(arr) - 1, 3) == 2
    assert binary_search(arr, 0, len(arr) - 1, 8) == 7
    assert binary_search(arr, 0, len(arr) - 1, 30) == -1

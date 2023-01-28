import logging
import os
from typing import List

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)


def bubble_sort(arr: List[int]):
    """
    As long as we're still making updates (in_progress), continue
    iterating through the array and bubbling-up the greater number.
    """
    logger = logging.getLogger("bubble_sort")
    n = len(arr)
    in_progress = True
    n_iter = 1  # just for inspection
    while in_progress:
        in_progress = False
        for i in range(n):
            j = i + 1
            if j == n:
                break
            elif arr[i] > arr[j]:
                in_progress = True
                arr[i], arr[j] = arr[j], arr[i]
        n_iter += 1
    logger.debug(f"Made {n_iter} trips through the input list")
    return arr


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    expected_output = sorted(numbers)
    assert bubble_sort(numbers) == expected_output

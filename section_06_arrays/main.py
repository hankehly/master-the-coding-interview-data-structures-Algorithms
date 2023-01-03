import logging
from typing import List

logger = logging.getLogger(__name__)


def reverse_string(src: str) -> str:
    """
    reverse_string("hello world")
    => "dlrow olleh"
    """
    src_rev = []
    n = len(src)
    for i in range(n):
        src_rev.append(src[n - 1 - i])
    return "".join(src_rev)


def merge_sorted_arrays_poor_time_complexity(a: List[int], b: List[int]) -> List[int]:
    """
    A naive approach with poor time complexity O(n^2)
    """
    c = []
    for item_a in a:
        for item_b in b:
            if item_b < item_a:
                c.append(item_b)
        c.append(item_a)
    return c


def merge_sorted_arrays_video_solution(a: List[int], b: List[int]) -> List[int]:
    """
    The solution proposed in the lecture video (BUG: an exception occurs if len(a) < len(b))
    """
    c = []
    a_i, b_i = 0, 0
    a_val, b_val = a[a_i], b[b_i]
    a_len, b_len = len(a), len(b)
    while a_val is not None or b_val is not None:
        logger.info(f"a_val: {a_val}, b_val: {b_val}")
        if b_val is None or a_val < b_val:
            logger.info(f"Appending a_val ({a_val}) to list.")
            c.append(a_val)
            a_i += 1
            a_val = a[a_i] if a_i < a_len else None
        else:
            logger.info(f"Appending b_val ({b_val}) to list.")
            c.append(b_val)
            b_i += 1
            b_val = b[b_i] if b_i < b_len else None
    return c


def merge_sorted_arrays(a: List[int], b: List[int]) -> List[int]:
    """
    Custom solution with O(n) time complexity and no list-length bug.
    Output shoudl be the same as `sorted(a + b)`

    merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30])
    => [0, 3, 4, 4, 6, 30, 31]
    """
    c = []
    a_i, b_i = 0, 0
    a_val, b_val = a[a_i], b[b_i]
    a_len, b_len = len(a), len(b)
    while a_val is not None or b_val is not None:
        logger.info(f"a_val: {a_val}, b_val: {b_val}")
        has_a = a_val is not None
        has_b = b_val is not None
        only_has_a = has_a and not has_b
        only_has_b = has_b and not has_a
        has_both = has_a and has_b
        if only_has_a or (has_both and a_val < b_val):
            logger.info(f"Appending a_val ({a_val}) to list.")
            c.append(a_val)
            a_i += 1
            a_val = a[a_i] if a_i < a_len else None
        elif only_has_b or (has_both and b_val < a_val):
            logger.info(f"Appending b_val ({b_val}) to list.")
            c.append(b_val)
            b_i += 1
            b_val = b[b_i] if b_i < b_len else None
        else:
            logger.info(f"Appending both a_val ({a_val}) and b_val ({b_val}) to list.")
            c.append(a_val)
            a_i += 1
            a_val = a[a_i] if a_i < a_len else None
            c.append(b_val)
            b_i += 1
            b_val = b[b_i] if b_i < b_len else None
    return c


def main():
    assert reverse_string("hello world") == "dlrow olleh"
    assert merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]) == [0, 3, 4, 4, 6, 30, 31]


if __name__ == "__main__":
    main()

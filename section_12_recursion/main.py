def find_factorial_recursive(n: int) -> int:
    """
    What's 3! ?
    It's 3 * 2!  << recursive case

    What's 2! ?
    It's 2 * 1!  << recursive case (actually 2! is also 2, so we can include this in our base case, but we don't have to)

    What's 1! ?
    It's 1!      << base case
    """
    if n == 1 or n == 2:  # 0 < n < 3
        return n
    return n * find_factorial_recursive(n - 1)


def find_factorial_iterative(n: int) -> int:
    answer = n

    # Using a while-loop
    i = n - 1
    while i > 0:
        answer = answer * i
        i -= 1

    # Using a for-loop
    # for i in range(n - 1, 0, -1):
    #     answer = answer * i

    return answer


if __name__ == "__main__":
    assert find_factorial_recursive(1) == find_factorial_iterative(1) == 1
    assert find_factorial_recursive(2) == find_factorial_iterative(2) == 2
    assert find_factorial_recursive(3) == find_factorial_iterative(3) == 6
    assert find_factorial_recursive(4) == find_factorial_iterative(4) == 24

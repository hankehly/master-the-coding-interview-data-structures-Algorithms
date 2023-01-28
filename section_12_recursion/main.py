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


def fibonacci_recursive(n) -> int:
    """
    O(2^n) (exponential time, very bad!)

    Return the n-th value of the Fibonacci sequence.
      0, 1, 1, 2, 3, 5, 8, 13, 21, ..

    Example:
      n=2, answer=1
      n=3, answer=2
      n=7, answer=13
    """
    assert n >= 0
    if n < 2:
        return n
    # What's the value of fib(3)?
    # It's fib(1) + fib(2)
    # Okay, what's the value of fib(4)?
    # Well, it's fib(2) + fib(3)
    return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


def fibonacci_iterative(n) -> int:
    """
    O(n)
    """
    assert n >= 0
    if n < 2:
        return n
    fib = [0, 1]
    # Ignore the first 2 indices, start from fib[2] and go until n (n+1 so that n is included)
    for i in range(2, n + 1):
        fib.append(fib[i - 2] + fib[i - 1])
    # Now that we have n numbers in the sequence, return the one we need
    return fib[n]


def reverse_string_iterative(string: str) -> str:
    a = list(string)
    for i in range(len(a) // 2):
        j = len(a) - (i + 1)
        a[i], a[j] = a[j], a[i]
    return "".join(a)


def reverse_string_recursive(string: str) -> str:
    """
    How can we divide this into smaller sub-problems?
    We can split the string in two, and swap the order.
    Keep doing this until we're left with one character.
    In that case, we can't split the problem any further, so return the character.

                                 hello
                                /    \
                              llo     he    # divide into 2, swap places
                              / \     / \
                            lo   l   e   h  # same thing
                            / \
                           o   l            # same thing
    """
    if len(string) == 1:
        return string
    mid_point = len(string) // 2
    front, back = string[:mid_point], string[mid_point:]
    return reverse_string_recursive(back) + reverse_string_recursive(front)


if __name__ == "__main__":
    # Factorial
    assert find_factorial_recursive(1) == find_factorial_iterative(1) == 1
    assert find_factorial_recursive(2) == find_factorial_iterative(2) == 2
    assert find_factorial_recursive(3) == find_factorial_iterative(3) == 6
    assert find_factorial_recursive(4) == find_factorial_iterative(4) == 24
    # Fibonacci
    assert fibonacci_recursive(3) == fibonacci_iterative(3) == 2
    assert fibonacci_recursive(2) == fibonacci_iterative(2) == 1
    assert fibonacci_recursive(7) == fibonacci_iterative(7) == 13
    assert fibonacci_recursive(8) == fibonacci_iterative(8) == 21
    # Reverse string
    # assert reverse_string_recursive("yoyo mastery") == "yretsam oyoy"
    print(reverse_string_recursive("yoyo mastery"))
    # assert reverse_string_iterative("yoyo mastery") == "yretsam oyoy"

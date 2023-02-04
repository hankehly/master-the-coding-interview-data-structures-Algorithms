def memoize(fn):
    cache = {}

    def wrapper(i):
        if i not in cache:
            cache[i] = fn(i)
        return cache[i]

    return wrapper


@memoize
def fib(i):
    if i < 2:
        return i
    return fib(i - 1) + fib(i - 2)


if __name__ == "__main__":
    assert fib(100) == 354224848179261915075

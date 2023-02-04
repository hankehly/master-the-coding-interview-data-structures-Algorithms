# Section 15: Algorithms: Dynamic Programming

Dynamic Programming is just a buzz word. It basically means *optimizing by using a cache*.

Can the problem be divided into sub-problems?
=> Use recursion

Are there repetitive sub-problems?
=> Use memoization

If a problem can be broken down into sub-problems, we can use recursion. If those sub-problems *overlap* a lot (doing the same problem over and over, like in the fibonacci function), use *memoization* to cache the return values.

As we solve problems, we can reuse those answers to solve bigger problems, and bigger problems.

### Memoization

Caching the return value of a function based on its parameters.
Now those parameters are *memoized*.
If the params are the same on subsequent calls, you return the cached value.
Memoizing can significantly decrease time complexity.

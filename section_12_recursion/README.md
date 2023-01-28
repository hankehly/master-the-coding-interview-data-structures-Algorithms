# Section 12: Algorithms: Recursion

Term | Meaning
:- | :-
Recursive Case | The case in a recursive function where you call the function again
Base Case | The case in a recursive function where you stop calling the function

Usually you have 2 returns – one for the base case and one for the recursive case.

### Figuring out the recursive case

When you're trying to figure out the recursive case, try to explain the answer by using the function itself. For example:
```
What's the value of f(5) ?
It's f(3) + f(4)                 # Use the function itself to explain the answer
Okay, what's the value of f(4)?  # Ask the question repeatedly and it becomes apparent how the recursion should work
It's f(2) + f(3)
...
```

Continue until you reach low numbers (nearing the base case). It should become apparent that the answer to a certain prompt is always going to be a specific value, like 1 or something.

```
What's the value of f(2) ?
It's 1, always               # This is your base case (if n==1)
What's the value of f(1) ?
It's 0, always               # This can also be part of the base case (if n==0)
```

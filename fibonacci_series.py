def fib_series(n):
    "Returns the number in which fibonacci series that given index"
    if n <= 0:
        return n
    return fib_series(n - 1) + fib_series(n - 2)



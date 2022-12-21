# Return nth number in Fibonacci sequence

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a
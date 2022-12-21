# Return nth number in Fibonacci sequence

def fibonacci(n):
    """
    This function takes in a number and will r
    :param n:
    :return:
    """
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_series(n, a=0, b=1):
    for _ in range(n):
        a, b = b, a + b
    return a
# Return nth number in Fibonacci sequence

def fibonacci(n):
    """
    This function takes in a number and uses it to return the nth number in the Fibonacci sequence.
    Note: Function assumes that the Fib series starts with 0.
    :param n:
    :return:
    """
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a


def lucas(n):
    """
    This function takes in a number and uses it to return the nth number in the Lucas Series.
    :param n:
    :return:
    """
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_series(n, a=0, b=1):
    """
    This function takes a required argument (n) as a number to return the nth value in the Fibonacci or Lucas series depending on the optional values input as a and b.
    The default values for a and b are 0, 1 respectively and will return the nth number in the Fibonacci sequence.
    To return the nth value from the Lucas series, the user will add in optional parameters of 2,1 for a,b respectively.
    :param n:
    :param a: 
    :param b:
    :return:
    """
    for _ in range(n):
        a, b = b, a + b
    return a
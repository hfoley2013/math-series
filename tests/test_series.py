from modules.series import fibonacci, lucas, sum_series

def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_4():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas_6():
    actual = lucas(6)
    expected = 18
    assert actual == expected

def test_sum_series_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_5_fib():
    acutal = sum_series(5)
    expected = 5
    assert acutal == expected

def test_sum_series_5_lucas():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected
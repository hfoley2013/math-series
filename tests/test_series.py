import pytest
from series import fibonacci, lucas


def test_fibonacci(n):
    actual = fibonacci(5)
    expected = "5"
    actual == expected


def test_lucas(n):
    actual = lucas(5)
    expected = "11"
    assert actual == expected
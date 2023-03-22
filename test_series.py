import pytest
from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci_function():
    assert fibonacci(1)

def test_fibonacci_function_argument_being_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_function_argument_being_7():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

def test_fibonacci_function_argument_being_10():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_lucas_function():
    assert lucas(1)

def test_lucas_function_with_argument_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_function_with_argument_8():
    actual = lucas(8)
    expected = 47
    assert actual == expected

def test_sum_series_function_with_required_argument_5():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

def test_sum_series_function_with_required_argument_and_both_optional_arguments_5():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected

def test_sum_series_function_with_required_argument_5_and_both_optional_arguments_that_are_not_0_and_1_or_2_and_1():
    actual = sum_series(5,4,9)
    expected = [5,11,36,6,2,1]
    assert actual == expected
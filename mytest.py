import pytest
import mycal


def test_check_it_return_addition():
    result = mycal.add(2, 3)
    assert result == 5

def test_check_it_return_subtraction():
    result = mycal.subtract(10, 4)
    assert result == 6

def test_check_it_return():
    result = mycal.multiply(5, 8)
    assert result == 40
import pytest
from app import add, subtract, multiply, divide, remainder_divide, floor_divide

def test_add():
    assert add(3, 2) == 5
    assert add(4, -1) == 3

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(2, -2) == -4

def test_divide():
    assert divide(4, 2) == 2
    assert divide(6, 3) == 2

def test_remainder_divide():
    assert remainder_divide(3, 3) == 0
    assert remainder_divide(5, 3) == 2

def test_floor_divide():
    assert floor_divide(4, 3) == 1
    assert floor_divide(4, 2) == 2

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(-1, 1) == 0

def test_fun2():
    assert calculator.fun2(5, 3) == 2
    assert calculator.fun2(0, 4) == -4

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(-2, 3) == -6

def test_fun4():
    assert calculator.fun4(2, 3) == 10
    assert calculator.fun4(0, 0) == 0

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, -1, -2),
])
def test_fun1_param(x, y, expected):
    assert calculator.fun1(x, y) == expected

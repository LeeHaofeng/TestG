import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from calc import add, div, mean

def test_add():
    assert add(2, 3) == 5

def test_div_zero():
    try:
        div(1, 0)
        assert False, "expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

def test_mean_floor():
    # mean of [2, 3] should be 2 (floor), docstring says integer-safe
    assert mean([2, 3]) == 2

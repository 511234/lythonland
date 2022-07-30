from pytest_playground.index import increment
import pytest


def test_positive():
    assert increment(2) == 4
    assert increment(3) == 6
    assert increment(4) == 8


def test_negative():
    assert increment(-2) == -4
    assert increment(-3) == -6
    assert increment(-4) == -8


def test_zero():
    assert increment(0) == 0


def test_dict():
    with pytest.raises(TypeError):
        increment({'x': 'y'})

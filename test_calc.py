import calc
import pytest


def test_add():
    assert calc.add(3, 4, 5) == 12
    assert calc.add(4, -4) == 0
    assert calc.add(2) == 2
    assert calc.add(0) == 0
    assert calc.add(-10, -400) == -410


def test_sub():
    assert calc.sub(3, 4) == -1
    assert calc.sub(5, 5) == 0
    assert calc.sub(-10, -10) == 0
    assert calc.sub(-4, 0) == -4
    assert calc.sub(-5, -7) == 2


def test_mult():
    assert calc.mult(-5, 5) == -25
    assert calc.mult(0, 5) == 0
    assert calc.mult(7, 0, 3) == 0
    assert calc.mult(-10, -10) == 100
    assert calc.mult(1, 1, 5) == 5

def test_div():
    with pytest.raises(Exception):
        x = calc.div(3, 0)
    assert calc.div(3, 1) == 3
    assert calc.div(5, 5) == 1
    assert calc.div(10, 5) == 2
    assert calc.div(5, 2) == 2.5

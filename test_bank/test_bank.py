from bank import value
import pytest

def test_hello():
    assert value("hello, jack") == 0
    assert value("Hello, damn") == 0
    assert value("hEllo") == 0

def test_h():
    assert value("Hijack!!") == 20
    assert value("hip pop") == 20
    assert value("herb") == 20

def test_shit():
    assert value("shit") == 100
    assert value("get_the_fuck_out_of_here") == 100
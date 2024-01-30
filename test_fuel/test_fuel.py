from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("8/0")
    assert convert("2/2") == 100
    assert convert("0/1") == 0


def test_aguge():
    assert gauge(25) == "25%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

import pytest
from numb3rs import validate


def test_invalidate():
    assert validate("255.255.255.256") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False


def test_validate():
    assert validate("255.255.255.25") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True

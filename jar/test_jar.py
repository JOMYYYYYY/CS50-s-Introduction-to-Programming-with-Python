from jar import Jar
import pytest
from unittest.mock import MagicMock


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    # jar.deposit(13)
    # assert str(jar) == ValueError
    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪"
    # jar.withdraw(2)
    # assert str(jar) == ValueError
    with pytest.raises(ValueError):
        jar.withdraw(2)
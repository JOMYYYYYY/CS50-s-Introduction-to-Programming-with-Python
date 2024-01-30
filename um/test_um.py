import pytest
from um import count

def test_1():
    assert count("um") == 1
    assert count("um...um") == 2
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_2():
    assert count("") == 0
    assert count("123") == 0
    assert count("yummy") == 0

def test_3():
    assert count("ooohno") == 0
    assert count(" um yummy um um") == 3

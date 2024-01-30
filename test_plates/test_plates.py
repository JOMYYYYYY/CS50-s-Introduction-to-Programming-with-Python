from plates import is_valid
import string
import pytest

def test_only_numbers():
    assert is_valid("1998") == False
    assert is_valid("911") == False

def test_length():
    assert is_valid("hihahi----------------------") == False
    assert is_valid("j") == False
    assert is_valid("CS50") == True

def test_middle_number():
    assert is_valid("j0k") == False
    assert is_valid("AAA222") == True
    assert is_valid("222AAA") == False
    assert is_valid("AAA22A") == False
    assert is_valid("cs012") == False

def test_marks():
    assert is_valid("cs50,") == False
    assert is_valid("...") == False
    assert is_valid("CS 90") == False
    assert is_valid("") == False
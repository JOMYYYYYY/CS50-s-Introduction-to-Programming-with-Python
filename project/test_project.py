import pytest
from project import count_price
from project import count_usage_amount
from project import suggestion
from io import StringIO
import sys


def test_count_usage_amount():
    assert count_usage_amount(200, 5, 10, 20) == 97500
    assert count_usage_amount(200, 5, 10, 10) == 195000
    assert count_usage_amount(50, 1, 50, 125) == 19600


def test_count_price():
    assert count_price(10, 20) == 200
    assert count_price(1, 20) == 20
    assert count_price(99, 20) == 1980
    assert count_price(2023, 1) == 2023


def test_suggestion():
    # Redirect stdout to a StringIO object
    stdout = StringIO()
    sys.stdout = stdout

    # Test case 1: Invalid parameter
    assert suggestion(0) is None
    output = stdout.getvalue()
    assert "Invalid parameter" in output

    # Test case 2: C type project
    assert suggestion(5000) == "C"
    output = stdout.getvalue()
    assert "This is a C type project." in output
    assert "the suggestion is: \"the suggestion content of C type project\"" in output

    # Test case 3: B type project
    assert suggestion(2500000) == "B"
    output = stdout.getvalue()
    assert "This is a B type project." in output
    assert "the suggestion is: \"the suggestion content of B type project\"" in output

    # Test case 4: A type project
    assert suggestion(10000000) == "A"
    output = stdout.getvalue()
    assert "This is an A type project." in output
    assert "the suggestion is: \"the suggestion content of A type project\"" in output

    # Restore stdout
    sys.stdout = sys.__stdout__


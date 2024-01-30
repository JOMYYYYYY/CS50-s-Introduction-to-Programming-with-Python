import pytest
import seasons


def test_check_input_validation():
    assert seasons.check_input_validation("1999-01-01") == True
    assert seasons.check_input_validation("cat") == False
    assert seasons.check_input_validation("19990901") == False
    assert seasons.check_input_validation("1999-09-45") == False

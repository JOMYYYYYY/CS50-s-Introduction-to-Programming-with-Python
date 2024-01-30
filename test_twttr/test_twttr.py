from twttr import shorten

def test_shorten():
    assert shorten("JIK") == "JK"
    assert shorten("aeIou") == ""
    assert shorten("tanyaxing") == "tnyxng"
    assert shorten("ioio") == ""
    assert shorten("123.") == "123."

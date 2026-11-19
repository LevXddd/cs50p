from working import convert
import pytest

def test_value_error():
    with pytest.raises(ValueError):
        convert("26 PM to 15 AM")


def test_valid_formats():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_text():
    with pytest.raises(ValueError):
        convert("cat")

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 PM to 5:60 AM")

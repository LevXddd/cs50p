from numb3rs import validate



def test_valid():
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("1.999.999.999") == False
    assert validate("255.0.0.256") == False

def test_out_of_range():
    assert validate("275.3.6.28") == False
    assert validate("545.545.656") == False


def test_text():
    assert validate("text") == False

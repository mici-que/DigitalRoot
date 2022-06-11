from DigitalRoot import main


# initial test
def test_init():
    """no input given, return False"""
    assert (main()) == False


# 1 input validation
def test_WrongInputType():
    """input is string, return False"""
    param = "1"
    assert (main(param)) == False


def test_WrongInputType2():
    """input is list, return False"""
    param = [
        1,
    ]
    assert (main(param)) == False


def test_NegativeNumber():
    """input is negative, return False"""
    param = -1
    assert (main(param)) == False


def test_ValidInput():
    """input is non-negative integer, should return integer"""
    param = 11
    assert isinstance(main(param), int) == True


def test_ValidInput2():
    """input is non-negative integer, return value should have one digit"""
    param = 11
    assert len(str(main(param))) == 1


def test_InputZero():
    """input is zero, should return zero"""
    param = 0
    assert main(param) == 0

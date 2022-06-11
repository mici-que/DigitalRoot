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
    assert 0 <= main(param) <= 9


def test_InputZero():
    """input is zero, should return zero"""
    param = 0
    assert main(param) == 0


# 2 Calculation
def test_ZeroAgain():
    """input is zero, return same"""
    param = 0
    assert main(param) == 0


def test_SingleDigit():
    """input is single digit, return same: 9=>9"""
    param = 9
    assert main(param) == 9


def test_TwoDigitsBelow10():
    """input has to digits, sum is below 10: 11=>2"""
    param = 11
    assert main(param) == 2


def test_ThreeDigitsBelow10():
    """input has three digits, sum is below 10: 112=>4"""
    param = 112
    assert main(param) == 4


def test_FourDigitsBelow10():
    """input has four digits, sum is below 10: 3000=>3"""
    param = 3000
    assert main(param) == 3


# 2b add tests where digital sum is bigger than 9


def test_TwoRoundsNeeded():
    """input is 99, should return 18"""
    param = 99
    assert main(param) == 9


def test_ThreeRoundsNeeded():
    """input is 493193, should return 2"""
    param = 493193
    assert main(param) == 2

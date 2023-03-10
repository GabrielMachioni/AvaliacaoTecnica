from main import BracketChecker
import pytest

@pytest.fixture
def bracket_checker():
    # Creating an instance with parameters '{[(' and '}])'.
    return BracketChecker('{[(', '}])')


def test_check_sequences(bracket_checker):
    # Tests the checker function with some sequences
    assert bracket_checker.check('{[()]}') == True
    assert bracket_checker.check('()[]{}') == True
    assert bracket_checker.check('([])') == True
    assert bracket_checker.check('{{[[(())]]}}') == True
    assert bracket_checker.check('{[()([])]}') == True
    assert bracket_checker.check('([]') == False
    assert bracket_checker.check('[({)}]') == False
    assert bracket_checker.check(')(') == False
    assert bracket_checker.check('(([{()}])))') == False


def test_check_another_sequences(bracket_checker):
    # Tests the checker function with some other sequences
    assert bracket_checker.check('()') == True
    assert bracket_checker.check('[]') == True
    assert bracket_checker.check('{}[]') == True
    assert bracket_checker.check('') == True
    assert bracket_checker.check(')(') == False
    assert bracket_checker.check('(){()') == False


def test_check_special_sequences(bracket_checker):
    # Test with some special sequences
    assert bracket_checker.check('(5)') == True
    assert bracket_checker.check('key[value]') == True
    assert bracket_checker.check('{teste}[teste]') == True

from main import StringChecker


def test_count_substrings():
    checker = StringChecker()

    # Test with substrings
    assert checker.count_substrings('CDC', 'ABCDCDC') == 2
    assert checker.count_substrings('22', '0222154') == 2
    assert checker.count_substrings('pyk', 'abc') == 0
    assert checker.count_substrings('XX', 'XXXxXXX') == 4
    
    # Test with other special substrings
    assert checker.count_substrings('*', 'hhh*hhh') == 1
    assert checker.count_substrings('++', 'test++test') == 1
    assert checker.count_substrings('*', '') == 0
    assert checker.count_substrings(' ', 'space   space') == 3


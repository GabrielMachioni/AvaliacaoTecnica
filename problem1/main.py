import re

class StringChecker:
    """
    Class responsible for check substring in strings
    """
    def count_substrings(self, s2, s1):
        escaped_s2 = re.escape(s2)
        count = len(re.findall(f"(?={escaped_s2})", s1))
        return count


if __name__ == "__main__":
    # input
    s1 = 'ABCDCDC'
    s2 = 'CDC'

    string_checker = StringChecker()
    print(string_checker.count_substrings(s2, s1))
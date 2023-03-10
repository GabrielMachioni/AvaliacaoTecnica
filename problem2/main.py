class BracketChecker:
    """
    Class reposible to check the brackets
    """
    def __init__(self, open_chars='({[', close_chars=')}]'):
        self.char_pairs = dict(zip(close_chars, open_chars))

    def check(self, seq):
        stack = []
        for char in seq:
            if char in self.char_pairs:
                if not stack:
                    return False
                if stack[-1] != self.char_pairs[char]:
                    return False
                stack.pop()
            elif char in self.char_pairs.values():
                stack.append(char)
        return not stack


if __name__ == '__main__':
    seq = "{[]()}"
    checker = BracketChecker()
    print(f'Solution: {checker.check(seq)}')
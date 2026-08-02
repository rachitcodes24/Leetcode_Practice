from functools import reduce

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return reduce(lambda ans, char: ans * 26 + ord(char) - 64, columnTitle, 0)
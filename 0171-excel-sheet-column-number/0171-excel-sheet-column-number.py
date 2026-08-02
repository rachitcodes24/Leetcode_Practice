class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for char in columnTitle:
            ans = ans * 26 + ord(char) - 64
        return ans
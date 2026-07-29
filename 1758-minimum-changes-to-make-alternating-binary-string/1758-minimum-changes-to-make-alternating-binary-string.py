class Solution:
    def minOperations(self, s: str) -> int:
        ans = sum(c != "01"[i % 2] for i, c in enumerate(s))
        return min(ans, len(s) - ans)
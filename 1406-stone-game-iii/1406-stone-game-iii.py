class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp1, dp2, dp3 = 0, 0, 0

        for i in range(n - 1, -1, -1):
            best = stoneValue[i] - dp1
            if i + 1 < n:
                best = max(best, stoneValue[i] + stoneValue[i + 1] - dp2)
            if i + 2 < n:
                best = max(best, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp3)

            dp1, dp2, dp3 = best, dp1, dp2

        if dp1 > 0:
            return "Alice"
        if dp1 < 0:
            return "Bob"
        return "Tie"
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans = 0
        push = 1
        
        while n > 0:
            ans += min(n, 8) * push
            n -= 8
            push += 1
            
        return ans
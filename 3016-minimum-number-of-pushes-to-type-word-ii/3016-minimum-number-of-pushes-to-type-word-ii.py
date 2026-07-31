from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = sorted(Counter(word).values(), reverse=True)
        total_pushes = 0
        
        for i, count in enumerate(counts):
            total_pushes += count * ((i // 8) + 1)
            
        return total_pushes
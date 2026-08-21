import math

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        filtered = []
        for c in coins:
            if not any(c % f == 0 for f in filtered):
                filtered.append(c)
        
        n = len(filtered)
        subsets = []
        
        for i in range(1, 1 << n):
            current_lcm = 1
            bits = 0
            for j in range(n):
                if (i >> j) & 1:
                    current_lcm = math.lcm(current_lcm, filtered[j])
                    bits += 1
            subsets.append((current_lcm, 1 if bits % 2 == 1 else -1))
            
        def count(x):
            return sum(sign * (x // val) for val, sign in subsets)

        left = 1
        right = filtered[0] * k
        
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
                
        return left
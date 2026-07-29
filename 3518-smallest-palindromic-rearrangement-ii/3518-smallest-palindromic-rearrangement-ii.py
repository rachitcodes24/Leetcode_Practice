import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        odd_char = ""
        half_counts = {}
        
        for char, count in counts.items():
            if count % 2 != 0:
                odd_char = char
            if count // 2 > 0:
                half_counts[char] = count // 2
                
        n = sum(half_counts.values())
        
        total_perms = 1
        rem = n
        for c in half_counts.values():
            total_perms *= math.comb(rem, c)
            rem -= c
            
        if k > total_perms:
            return ""
            
        chars = sorted(half_counts.keys())
        half_res = []
        
        for _ in range(n):
            for char in chars:
                if half_counts[char] == 0:
                    continue
                
                perms_if_picked = total_perms * half_counts[char] // n
                
                if k <= perms_if_picked:
                    half_res.append(char)
                    total_perms = perms_if_picked
                    half_counts[char] -= 1
                    n -= 1
                    break
                else:
                    k -= perms_if_picked
                    
        half_str = "".join(half_res)
        return half_str + odd_char + half_str[::-1]
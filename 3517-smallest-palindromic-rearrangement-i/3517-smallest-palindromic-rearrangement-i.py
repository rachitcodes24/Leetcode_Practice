from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        
        half = []
        mid = ""
        
        for char in sorted(freq.keys()):
            count = freq[char]
            
            half.append(char * (count // 2))
            
            if count % 2 != 0:
                mid = char
                
        first_half = "".join(half)
        
        
        return first_half + mid + first_half[::-1]
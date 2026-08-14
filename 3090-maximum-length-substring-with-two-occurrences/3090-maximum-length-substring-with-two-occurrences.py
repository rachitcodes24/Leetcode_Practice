class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        counts = {}
        
        for right in range(len(s)):
            # Add the current character to our frequency map
            counts[s[right]] = counts.get(s[right], 0) + 1
            
            # If the character count exceeds 2, shrink the window from the left
            while counts[s[right]] > 2:
                counts[s[left]] -= 1
                left += 1
                
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len
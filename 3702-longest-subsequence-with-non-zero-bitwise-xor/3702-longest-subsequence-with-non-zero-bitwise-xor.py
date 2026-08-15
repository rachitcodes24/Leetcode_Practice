class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        all_zeroes = True
        
        # Calculate the total XOR and check if the array is entirely zeroes
        for num in nums:
            total_xor ^= num
            if num != 0:
                all_zeroes = False
                
        # Case 1: Impossible to get a non-zero XOR
        if all_zeroes:
            return 0
            
        # Case 2: The whole array is already valid
        if total_xor != 0:
            return len(nums)
            
        # Case 3: The total XOR is 0, so we just remove one non-zero element
        return len(nums) - 1
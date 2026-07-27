class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        
        for num in nums:
            if num > max1:
                # Demote the current max1 to max2, and update max1
                max2 = max1
                max1 = num
            elif num > max2:
                # If it's not greater than max1 but is greater than max2, just update max2
                max2 = num
                
        return (max1 - 1) * (max2 - 1)
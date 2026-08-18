class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: k is the size of the array
        if k == n:
            return max(nums)
            
        # Case 2: k is 1
        if k == 1:
            counts = {}
            for num in nums:
                counts[num] = counts.get(num, 0) + 1
            
            ans = -1
            for num, count in counts.items():
                if count == 1:
                    ans = max(ans, num)
            return ans
            
        # Case 3: k is strictly between 1 and n
        ans = -1
        
        # Check first element
        if nums.count(nums[0]) == 1:
            ans = max(ans, nums[0])
            
        # Check last element
        if nums.count(nums[-1]) == 1:
            ans = max(ans, nums[-1])
            
        return ans
from functools import cache
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def get_max_diff(left: int, right: int) -> int:
            # Base case: only one element left to pick
            if left == right:
                return nums[left]
            
            # Option 1: Pick the leftmost number and subtract the opponent's best outcome
            pick_left = nums[left] - get_max_diff(left + 1, right)
            
            # Option 2: Pick the rightmost number and subtract the opponent's best outcome
            pick_right = nums[right] - get_max_diff(left, right - 1)
            
            # Each player plays optimally to maximize their net score difference
            return max(pick_left, pick_right)
        
        # Player 1 wins if their final score difference is 0 or greater
        return get_max_diff(0, len(nums) - 1) >= 0
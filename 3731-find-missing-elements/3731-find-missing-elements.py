class Solution:

  def findMissingElements(self, nums: List[int]) -> List[int]:
    num_set = set(nums)
    low, high = min(nums), max(nums)

    return [num for num in range(low, high + 1) if num not in num_set]
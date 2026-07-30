class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        invert_count = (k // (k & -k)) >> 1
        return "1" if (invert_count & 1) ^ ((k & 1) == 0) else "0"
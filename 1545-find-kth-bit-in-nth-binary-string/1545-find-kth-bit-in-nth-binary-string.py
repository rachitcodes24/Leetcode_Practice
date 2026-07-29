class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return str((k // (k & -k) >> 1 & 1) ^ (~k & 1))
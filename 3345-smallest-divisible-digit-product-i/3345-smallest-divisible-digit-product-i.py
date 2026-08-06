from math import prod

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while prod(int(d) for d in str(n)) % t != 0:
            n += 1
        return n
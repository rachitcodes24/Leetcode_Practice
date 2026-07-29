class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        col_sums = [sum(col) for col in zip(*mat)]
        return sum(col_sums[row.index(1)] == 1 for row in mat if sum(row) == 1)
class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        row_sums = [sum(row) for row in mat]
        col_sums = [sum(col) for col in zip(*mat)]
        
        special_count = 0
        for i, row in enumerate(mat):
            if row_sums[i] == 1:
                j = row.index(1)
                if col_sums[j] == 1:
                    special_count += 1
                    
        return special_count
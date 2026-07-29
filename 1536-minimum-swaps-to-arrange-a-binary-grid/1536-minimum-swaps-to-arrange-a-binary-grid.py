class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        zeros = []
        for row in grid:
            count = 0
            for val in row[::-1]:
                if val == 0:
                    count += 1
                else:
                    break
            zeros.append(count)
            
        ans = 0
        for i in range(n):
            target = n - 1 - i
            j = i
            while j < n and zeros[j] < target:
                j += 1
                
            if j == n:
                return -1
                
            ans += j - i
            zeros.insert(i, zeros.pop(j))
            
        return ans
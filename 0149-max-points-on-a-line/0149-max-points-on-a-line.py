import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        res = 1
        for i, (x1, y1) in enumerate(points):
            slopes = defaultdict(int)
            for x2, y2 in points[i + 1:]:
                dx, dy = x2 - x1, y2 - y1
                
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                    
                g = math.gcd(dx, dy)
                slopes[(dx // g, dy // g)] += 1
            
            if slopes:
                res = max(res, max(slopes.values()) + 1)
                
        return res
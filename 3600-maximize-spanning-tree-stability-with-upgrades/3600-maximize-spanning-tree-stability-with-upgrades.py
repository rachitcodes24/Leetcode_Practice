from typing import List


class Solution:
    def maxStability(
        self, n: int, edges: List[List[int]], k: int
    ) -> int:
        parent = list(range(n))
        rank = [0] * n
        components = n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> bool:
            nonlocal components
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
            components -= 1
            return True

        mandatory = []
        optional = []
        min_mandatory = float("inf")
        max_strength = 0

        for u, v, s, must in edges:
            if must == 1:
                if not union(u, v):
                    return -1
                mandatory.append((u, v, s))
                if s < min_mandatory:
                    min_mandatory = s
                if s > max_strength:
                    max_strength = s
            else:
                optional.append((u, v, s))
                if s * 2 > max_strength:
                    max_strength = s * 2

        for u, v, s in optional:
            union(u, v)

        if components > 1:
            return -1

        def check(target: int) -> bool:
            if target > min_mandatory:
                return False

            p = list(range(n))
            r = [0] * n
            comp = n

            def f(x: int) -> int:
                while p[x] != x:
                    p[x] = p[p[x]]
                    x = p[x]
                return x

            def u_op(x: int, y: int) -> bool:
                nonlocal comp
                rx, ry = f(x), f(y)
                if rx == ry:
                    return False
                if r[rx] < r[ry]:
                    rx, ry = ry, rx
                p[ry] = rx
                if r[rx] == r[ry]:
                    r[rx] += 1
                comp -= 1
                return True

            for u, v, s in mandatory:
                u_op(u, v)

            if comp == 1:
                return True

            for u, v, s in optional:
                if s >= target:
                    u_op(u, v)

            if comp == 1:
                return True

            upgrades = 0
            for u, v, s in optional:
                if s * 2 >= target and s < target:
                    if u_op(u, v):
                        upgrades += 1
                        if upgrades > k:
                            return False
                        if comp == 1:
                            return True

            return comp == 1 and upgrades <= k

        left = 1
        right = int(min(min_mandatory, max_strength))
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
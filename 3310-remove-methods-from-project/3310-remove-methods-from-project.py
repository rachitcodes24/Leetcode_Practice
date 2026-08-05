class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        suspicious = [False] * n
        suspicious[k] = True
        stack = [k]

        while stack:
            curr = stack.pop()
            for nxt in adj[curr]:
                if not suspicious[nxt]:
                    suspicious[nxt] = True
                    stack.append(nxt)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        return [i for i in range(n) if not suspicious[i]]
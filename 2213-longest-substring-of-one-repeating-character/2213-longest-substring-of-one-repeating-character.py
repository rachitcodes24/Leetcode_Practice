from typing import List

class Node:
    def __init__(self, size: int, pref_len: int, suff_len: int, max_len: int, pref_char: str, suff_char: str):
        self.size = size
        self.pref_len = pref_len
        self.suff_len = suff_len
        self.max_len = max_len
        self.pref_char = pref_char
        self.suff_char = suff_char

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)
        
        def merge(left: Node, right: Node) -> Node:
            if not left: return right
            if not right: return left
            
            size = left.size + right.size
            pref_char = left.pref_char
            suff_char = right.suff_char
            
            # Calculate prefix length
            pref_len = left.pref_len
            if left.pref_len == left.size and left.suff_char == right.pref_char:
                pref_len = left.size + right.pref_len
                
            # Calculate suffix length
            suff_len = right.suff_len
            if right.suff_len == right.size and left.suff_char == right.pref_char:
                suff_len = right.size + left.suff_len
                
            # Calculate overall max length
            max_len = max(left.max_len, right.max_len)
            if left.suff_char == right.pref_char:
                max_len = max(max_len, left.suff_len + right.pref_len)
                
            return Node(size, pref_len, suff_len, max_len, pref_char, suff_char)

        def build(node: int, start: int, end: int):
            if start == end:
                char = s[start]
                tree[node] = Node(1, 1, 1, 1, char, char)
                return
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def update(node: int, start: int, end: int, idx: int, char: str):
            if start == end:
                tree[node] = Node(1, 1, 1, 1, char, char)
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node + 1, start, mid, idx, char)
            else:
                update(2 * node + 2, mid + 1, end, idx, char)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        # Build the initial segment tree
        build(0, 0, n - 1)
        
        ans = []
        # Process each query
        for idx, char in zip(queryIndices, queryCharacters):
            update(0, 0, n - 1, idx, char)
            # The root node will always contain the max length for the whole string
            ans.append(tree[0].max_len)
            
        return ans
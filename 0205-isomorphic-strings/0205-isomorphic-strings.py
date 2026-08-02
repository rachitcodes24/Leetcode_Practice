class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2 = [0] * 256, [0] * 256
        for i, (c1, c2) in enumerate(zip(s, t), 1):
            o1, o2 = ord(c1), ord(c2)
            if m1[o1] != m2[o2]:
                return False
            m1[o1] = m2[o2] = i
        return True
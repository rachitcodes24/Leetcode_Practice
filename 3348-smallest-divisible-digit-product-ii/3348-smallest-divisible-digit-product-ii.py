from functools import cache

FACTORS = {
    1: (0, 0, 0, 0),
    2: (1, 0, 0, 0),
    3: (0, 1, 0, 0),
    4: (2, 0, 0, 0),
    5: (0, 0, 1, 0),
    6: (1, 1, 0, 0),
    7: (0, 0, 0, 1),
    8: (3, 0, 0, 0),
    9: (0, 2, 0, 0),
}


@cache
def min_len_23(r2: int, r3: int) -> int:
    if r2 <= 0 and r3 <= 0:
        return 0
    res = float("inf")
    if r2 > 0:
        res = min(
            res,
            1 + min_len_23(r2 - 3, r3),
            1 + min_len_23(r2 - 2, r3),
            1 + min_len_23(r2 - 1, r3),
        )
    if r3 > 0:
        res = min(
            res,
            1 + min_len_23(r2, r3 - 2),
            1 + min_len_23(r2, r3 - 1),
        )
    if r2 > 0 and r3 > 0:
        res = min(res, 1 + min_len_23(r2 - 1, r3 - 1))
    return res


def min_len(r2: int, r3: int, r5: int, r7: int) -> int:
    return max(0, r5) + max(0, r7) + min_len_23(max(0, r2), max(0, r3))


def build_suffix(rem_len: int, r2: int, r3: int, r5: int, r7: int) -> str:
    res = []
    for _ in range(rem_len):
        for dig in range(1, 10):
            f2, f3, f5, f7 = FACTORS[dig]
            nr2, nr3, nr5, nr7 = r2 - f2, r3 - f3, r5 - f5, r7 - f7
            if min_len(nr2, nr3, nr5, nr7) <= rem_len - 1 - len(res):
                res.append(str(dig))
                r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                break
    return "".join(res)


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        t2 = t3 = t5 = t7 = 0
        temp = t
        while temp % 2 == 0:
            t2 += 1
            temp //= 2
        while temp % 3 == 0:
            t3 += 1
            temp //= 3
        while temp % 5 == 0:
            t5 += 1
            temp //= 5
        while temp % 7 == 0:
            t7 += 1
            temp //= 7
        if temp > 1:
            return "-1"

        n = len(num)
        first_zero = num.find("0")
        if first_zero == -1:
            first_zero = n

        pref = [(0, 0, 0, 0)]
        for i in range(first_zero):
            c2, c3, c5, c7 = FACTORS[int(num[i])]
            p2, p3, p5, p7 = pref[-1]
            pref.append((p2 + c2, p3 + c3, p5 + c5, p7 + c7))

        if first_zero == n:
            p2, p3, p5, p7 = pref[n]
            if p2 >= t2 and p3 >= t3 and p5 >= t5 and p7 >= t7:
                return num

        for i in range(min(first_zero, n - 1), -1, -1):
            p2, p3, p5, p7 = pref[i]
            for d in range(int(num[i]) + 1, 10):
                f2, f3, f5, f7 = FACTORS[d]
                rem2 = t2 - (p2 + f2)
                rem3 = t3 - (p3 + f3)
                rem5 = t5 - (p5 + f5)
                rem7 = t7 - (p7 + f7)
                rem_len = n - 1 - i
                if min_len(rem2, rem3, rem5, rem7) <= rem_len:
                    return (
                        num[:i]
                        + str(d)
                        + build_suffix(rem_len, rem2, rem3, rem5, rem7)
                    )

        total_len = max(n + 1, min_len(t2, t3, t5, t7))
        return build_suffix(total_len, t2, t3, t5, t7)
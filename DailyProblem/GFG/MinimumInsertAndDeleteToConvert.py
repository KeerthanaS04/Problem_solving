from bisect import bisect_left
class Solution:
    def minInsAndDel(self, a, b):
        pos_map = {num:i for i, num in enumerate(b)}
        res = []

        for num in a:
            if num in pos_map:
                continue

            idx = pos_map[num]
            pos = bisect_left(res, idx)

            if pos == len(res):
                res.append(idx)
            else:
                res[pos] = idx
        common = len(res)
        return len(a) - common + len(b) - common
from collections import defaultdict
from bisect import bisect_left, bisect_right
class Solution:
    def freqInRange(self, arr, queries):
        pos = defaultdict(list)
        for i, num in enumerate(arr):
            pos[num].append(i)
        ans = []
        for l, r, x in queries:
            indices = pos.get(x, [])
            left = bisect_left(indices, l)
            right = bisect_right(indices, r)
            ans.append(right - left)
        return ans
from collections import defaultdict
from typing import List
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9+7
        cnt = defaultdict(int)

        for x, y in points:
            cnt[y]+=1
        result = 0
        total = 0

        for c in cnt.values:
            curr = (c*(c-1))//2
            result+=(result+curr*total)%MOD
            total=(total+curr)%MOD
        return result
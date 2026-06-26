from typing import List
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # prefix sums
        pref = []
        s = 0
        for x in nums:
            s+=1 if x == target else -1
            pref.append(s)

        # coordinate compression
        vals = sorted(set(pref+[0]))
        idx = {v:i+1 for i,v in enumerate(vals)}

        # fenwick tree
        m = len(vals)
        bit = [0]*(m+2)

        def update(i, delta):
            while i < m:
                bit[i] += delta
                i+=i & -i
        
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i-=i & -i
            return res
        
        ans = 0
        update(idx[0], 1)
        for p in pref:
            ans+=query(idx[p]-1)
            update(idx[p], 1)
        return ans
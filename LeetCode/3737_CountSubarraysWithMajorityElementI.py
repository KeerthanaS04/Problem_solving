from typing import List
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        fenwick_size = 2*n+5
        fenwick = [0]*fenwick_size
        offset = n+2
        balance = 0
        result = 0
        def update(index, value):
            while index < fenwick_size:
                fenwick[index] += value
                index+=index & -index

        def prefix_sum(index):
            s = 0
            while index > 0:
                s += fenwick[index]
                index-=index & -index
            return s
        update(offset, 1)
        for num in nums:
            if num == target:
                balance += 1
            else:
                balance -= 1
            result+=prefix_sum(offset+balance-1)
            update(offset+balance, 1)
        return result
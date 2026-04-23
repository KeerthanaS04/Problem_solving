from typing import List
from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        val_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            val_to_indices[val].append(i)
        
        res = [0]*len(nums)

        for indices in val_to_indices.values():
            left_sum = 0
            right_sum = sum(indices)-len(indices)*indices[0]

            for i in range(len(indices)):
                res[indices[i]] = left_sum+right_sum

                if i+1<len(indices):
                    gap = indices[i+1]-indices[i]
                    left_sum = gap*(i+1)
                    right_sum = gap*(len(indices)-i-1)
        return res
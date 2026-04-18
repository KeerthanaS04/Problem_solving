from collections import Counter
from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Initialize with starting window
        element_count = Counter(nums[:k])
        curr_sum = sum(nums[:k])
        max_sum = curr_sum if len(element_count)==k else 0

        for i in range(k, len(nums)):
            element_count[nums[i]]+=1
            # remove the leftmost element
            element_count[nums[i-k]]-=1

            # if count becomes 0, remove the element from the counter entirely
            if element_count[nums[i-k]]==0:
                element_count.pop(nums[i-k])
            
            curr_sum+=nums[i] - nums[i-k]

            if len(element_count)==k:
                max_sum = max(max_sum, curr_sum)
        return max_sum
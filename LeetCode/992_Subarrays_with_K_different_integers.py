"""
Number of integers in that array is exactly k
"""
from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost_k(k):
            if k==0:
                return 0

            left = 0
            count = 0
            freq = defaultdict(int)
            distinct = 0

            for right in range(len(nums)):
                if freq[nums[right]] == 0:
                    distinct += 1
                freq[nums[right]] += 1

                while distinct>k:
                    freq[nums[left]] -= 1

                    if freq[nums[left]]==0:
                        distinct -= 1
                    left += 1
                
                count += right-left+1

            return count
        return atmost_k(k)-atmost_k(k-1)
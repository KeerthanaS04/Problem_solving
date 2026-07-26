from typing import List

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        def find_xth_smallest_negative(x:int) -> int:
            count = 0
            # iterate through negative numbers only
            for i in range(50):
                count+=freq_count[i]
                if count>=x:
                    return i-50
            return 0

        freq_count = [0]*101
        for val in nums[:k]:
            freq_count[val+50]+=1

        res = find_xth_smallest_negative(x)

        for i in range(k, len(nums)):
            freq_count[nums[i]+50]+=1
            # remove the left-most element
            freq_count[nums[i-k]+50]-=1
            res.append(find_xth_smallest_negative(x))
        return res
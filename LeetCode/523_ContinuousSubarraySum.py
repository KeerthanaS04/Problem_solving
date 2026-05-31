from typing import List
class Solution:
    def checkSubarray(self, nums: List[int], k: int) -> bool:
        remainder_to_idx = {0:-1}
        running_sum = 0

        for idx, num in enumerate(nums):
            running_sum = (running_sum+num)%k

            if running_sum not in remainder_to_idx:
                remainder_to_idx[running_sum]=idx
            # if remainder was seen before and subarray length is atleast 2
            elif idx-remainder_to_idx[running_sum]>1:
                return True
        return False
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def format_range(start_idx: int, end_idx: int) -> str:
            if start_idx==end_idx:
                return str(nums[start_idx])
            return f'{nums[start_idx]}->{nums[end_idx]}'
        curr_idx = 0
        n = len(nums)
        res = []

        while curr_idx<n:
            range_end_idx = curr_idx

            while range_end_idx<n and nums[range_end_idx+1]==nums[range_end_idx]+1:
                range_end_idx+=1
            res.append(format_range(curr_idx, range_end_idx))
            curr_idx = range_end_idx+1
        return res
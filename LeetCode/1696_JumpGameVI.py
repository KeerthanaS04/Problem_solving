from typing import List
from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        deque_indices = deque([0])

        for i in range(n):
            # remove the indices that's outside the range
            if i-deque_indices[0]>k:
                deque_indices.popleft()
            
            # calculate maximum score for curr position
            dp[i] = nums[i]+dp[deque_indices[0]]

            # remove indices with smaller or equal dp values from the back
            while deque_indices and dp[deque_indices[-1]]<=dp[i]:
                deque_indices.pop()
            deque_indices.append(i)
        return dp[-1]
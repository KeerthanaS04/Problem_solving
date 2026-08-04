from typing import List
class Solution:
    def countPairs(self, arr: List[int], k: int) -> int:
        arr.sort()
        cnt = 0
        i = 0

        for j in range(1, len(arr)):
            while arr[j] - arr[i] >= k:
                i += 1
            cnt += (j - i)
        return cnt
from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0] * n
        suff = [0] * n

        pre[0] = arr[0]
        for i in range(1, n):
            pre[i] = max(arr[i], pre[i - 1] + arr[i])

        suff[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = max(arr[i], arr[i] + suff[i + 1])
        
        ans = max(pre)

        # maximum sum after deleting one element
        # best subarray ending before i with the best subarray starting after i
        for i in range(1, n - 1):
            ans = max(ans, pre[i-1]+suff[i+1])
        return ans
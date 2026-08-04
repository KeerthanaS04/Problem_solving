from typing import List
class Solution:
    def maxSumwithK(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = [0] * n
        res[0] = arr[0]

        for i in range(1, n):
            res[i] = max(arr[i], res[i-1] + arr[i])

        # sum of first k elements
        window_sum = sum(arr[:k])
        ans = window_sum

        for i in range(k, n):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            ans = max(ans, window_sum)

            left_idx = i-k
            ans = max(ans, window_sum + res[left_idx])
        return ans
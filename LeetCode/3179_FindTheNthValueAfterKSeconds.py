class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        arr = [1]*n
        MOD = 10**9+7

        for second in range(k):
            # prefix sum
            for idx in range(1, n):
                arr[idx] = (arr[idx]+arr[idx-1])%MOD
        return arr[n-1]
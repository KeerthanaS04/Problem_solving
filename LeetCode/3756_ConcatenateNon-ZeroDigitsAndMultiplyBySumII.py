from bisect import bisect_left, bisect_right
from typing import List
class Solution:
    def sumAnMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))
        
        k = len(digits)
        # powers of 10
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
        
        # prefix concatenated values
        pref_val = [0] * (k + 1)
        pref_sum = [0] * (k + 1)
        for i in range(k):
            pref_val[i + 1] = (pref_val[i] * 10 + digits[i]) % MOD
            pref_sum[i+1] = pref_sum[i] + digits[i]
        
        ans = []
        for l, r in queries:
            # find the range of non-zero digits in the substring s[l:r+1]
            left = bisect_left(pos, l)
            right = bisect_right(pos, r)
            
            if left == right:
                ans.append(0)
                continue

            length = right - left
            val = (pref_val[right] - pref_val[left] * pow10[length]) % MOD
            digit_sum = pref_sum[right] - pref_sum[left]
            ans.append((val * digit_sum) % MOD)
        
        return ans
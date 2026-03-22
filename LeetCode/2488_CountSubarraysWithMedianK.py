from typing import List
from collections import Counter
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        k_index = nums.index(k)
        right_balance_count = Counter()
        result = 1

        balance = 0
        for num in nums:
            if num>k:
                balance+=1
            else:
                balance-=1
            if 0<=balance<=1:
                result+=1
            right_balance_count[balance]+=1
        
        balance = 0
        for j in range(k_index-1, -1, -1):
            if nums[j]>k:
                balance+=1
            else:
                balance-=1
            
            if 0<=balance<=1:
                result+=1

            # we took the right balances that complement the left balances
            result+=right_balance_count[-balance]+right_balance_count[-balance+1]
        return result
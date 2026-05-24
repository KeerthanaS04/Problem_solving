from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            complement = target-numbers[i]
            l, r = i+1, n-1
            first_true_idx = -1

            while l<=r:
                mid = (l+r)//2
                if numbers[mid]>=target:
                    first_true_idx=mid
                    r=mid-1
                else:
                    l=mid+1
            
            if first_true_idx!=-1 and numbers[first_true_idx]==complement:
                return [i+1, first_true_idx+1]
        return []
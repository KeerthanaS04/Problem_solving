from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        sorted_array = sorted(nums)
        n = len(sorted_array)
        l = (n-1)//2
        r = n-1

        for idx in range(n):
            # even indices get elements from smaller half (backwards from middle)
            # odd indices get elements from larger half (backwards from end)
            if idx%2==0:
                nums[idx] = sorted_array[l]
                l -= 1
            else:
                nums[idx] = sorted_array[r]
                r -= 1
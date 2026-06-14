from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(left: int, right: int) -> int:
            # base case: single element
            if left == right:
                return nums[left]
            i, j = left-1, right+1
            pivot = nums[(left+right)//2]

            while i < j:
                # moving i forward until we find an element>pivot
                while True:
                    i += 1
                    if nums[i] > pivot:
                        break
                # moving j backward until we find an element<pivot
                while True:
                    j -= 1
                    if nums[j] < pivot:
                        break
                
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            # determine which partition contains the target idx
            if j<target_idx:
                return quicksort(j+1, right)
            else:
                return quicksort(left, j)
        n = len(nums)
        target_idx = n-k
        return quicksort(0, n-1)
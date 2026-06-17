from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort_count(l: int, r: int) -> int:
            if l>=r:
                return 0
            mid = (l+r)//2
            count = mergeSort_count(l, mid) + mergeSort_count(mid+1, r)

            # count reverse pairs across the two sorted halves
            i, j = l, mid+1
            while i<=mid and j<=r:
                if nums[i]<=2*nums[j]:
                    i+=1
                else:
                    count+=mid-i+1
                    j+=1
            
            # merge the two sorted halves
            temp = []
            i, j = l, mid+1
            while i<=mid and j<=r:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            # add remaining elements from left half
            temp.extend(nums[i:mid+1])
            # add remaining elements from right half
            temp.extend(nums[j:r+1])
            # copy sorted elements to back original array
            nums[l:r+1] = temp
            return count
        return mergeSort_count(0, len(nums)-1)
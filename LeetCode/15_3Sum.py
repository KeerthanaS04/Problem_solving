from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            # early termination: if the smallest number is positive, no zero sum possible
            if nums[i]>0:
                break

            # skip duplicate values for the first element to avoid duplicate triplets
            if i>0 and nums[i]==nums[i-1]:
                continue

            l, r = 0, n-1

            while l<r:
                curr_sum = nums[i]+nums[l]+nums[r]

                if curr_sum<0:
                    l+=1
                elif curr_sum>0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1

                    # skip duplicates for the second element
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    
                    # skip duplicates for the third element
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return res
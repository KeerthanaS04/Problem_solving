from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        if n<4:
            return res
        nums.sort()

        # first pointer: iterate through array leaving space for 3 more elements
        for i in range(n-3):
            # skip duplicates for the first element
            if i>0 and nums[i]==nums[i-1]:
                continue

            # second pointer: iterate from i+1 leaving the space for two more elements
            for j in range(i+1, n-2):
                # skip duplicates for the second element
                if j>i+1 and nums[j]==nums[j-1]:
                    continue

                l, r = j+1, n-1

                while l<r:
                    curr_sum = nums[i]+nums[j]+nums[l]+nums[r]

                    if curr_sum<target:
                        l+=1
                    elif curr_sum>target:
                        r-=1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        r-=1

                        # skip duplicates for the third element
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        # skip duplicates for the fourth element
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
        return res
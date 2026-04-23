from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total%2!=0:
            return False
        target = total//2
        possible = {0}

        for num in nums:
            new_possible = set()

            for s in possible:
                if s+num==target:
                    return True
                new_possible.add(s+num)
            possible|=new_possible
        return target in possible
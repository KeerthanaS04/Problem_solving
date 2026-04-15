from typing import List
class Solution:
    def sortedSquare(self, nums: List[int]) -> List[int]:
        res = []
        left = 0
        right = len(nums)-1

        while left<=right:
            left_sq = nums[left]*nums[left]
            right_sq = nums[right]*nums[right]

            if left_sq>=right_sq:
                res.append(left_sq)
                left+=1
            else:
                res.append(right_sq)
                right-=1
        return res[::-1]
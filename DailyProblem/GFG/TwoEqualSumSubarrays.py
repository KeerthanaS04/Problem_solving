class Solution:
    def canSplit(self, arr):
        total = sum(arr)

        if total%2!=0:
            return False
        
        target = total//2
        curr_sum = 0

        for num in arr:
            curr_sum+=num
            if curr_sum==target:
                return True
        return False
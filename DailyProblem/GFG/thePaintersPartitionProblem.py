class Solution:
    def minTime(self, arr, k):
        total = sum(arr)
        left = 0
        right = total
        ans = -1

        while left<=right:
            mid = left + (right-left)//2
            if self.check(mid, arr, k):
                ans = mid
                right = mid-1
            else:
                left = mid+1

        return ans
    
    def check(self, mid, arr, k):
        curr_allocation = mid
        painters = 1

        for board in arr:
            if curr_allocation>=board:
                curr_allocation-=board
            else:
                painters+=1
                if painters>k:
                    return False
                curr_allocation = mid

                if curr_allocation>=board:
                    curr_allocation-=board
                else:
                    return False
        return True
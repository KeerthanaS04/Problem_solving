class Solution:
    def binarySearchable(self, arr):
        # divide and conquer
        # everything in the left subtree must be smaller than the curr middle element
        # everything in the right subtree must be larger than the curr middle element
        n = len(arr)

        def helper(l, h, low, high):
            if l > h:
                return 0
            mid = l + (h - l) // 2
            curr = 0
            if low<arr[mid]<high:
                curr = 1
            
            left = helper(l, mid-1, low, min(high, arr[mid]))
            right = helper(mid+1, h, max(low, arr[mid]), high)
            return left + right + curr
        return helper(0,n-1,float('-inf'),float('inf'))
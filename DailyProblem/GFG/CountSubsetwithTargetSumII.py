from collections import Counter
class Solution:
    def countSubset(self, arr, k):
        n = len(arr)
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]

        def gen_sums(nums):
            sums = [0]
            for num in nums:
                sums+= [num+s for s in sums]
            return sums
        
        left_sums = gen_sums(left)
        right_sums = gen_sums(right)

        right_count = Counter(right_sums)
        ans = 0

        for s in left_sums:
            ans += right_count[k-s]
        return ans
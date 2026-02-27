class Solution:
    def longestSubarray(self, arr, k):
        prefix_index = {0: -1}
        prefix_sum = 0
        max_len = 0

        for i, val in enumerate(arr):
            if val>k:
                prefix_sum+=1
            else:
                prefix_sum-=1

            if prefix_sum>0:
                max_len = i+1 # valid subarray

            if (prefix_sum-1) in prefix_index:
                max_len = max(max_len, i-prefix_index[prefix_sum-1])
            
            if prefix_sum not in prefix_index:
                prefix_index[prefix_sum] = i
        return max_len
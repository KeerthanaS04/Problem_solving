class Solution:
    def maxSubstring(self, s):
        # using kadane's algorithm
        max_so_far = -1
        curr_sum = 0

        for c in s:
            val = 1 if c == '0' else -1
            curr_sum += val

            max_so_far = max(max_so_far, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_so_far
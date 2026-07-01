class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen_idx = {'a': -1, 'b': -1, 'c': -1}
        total_count = 0

        for i, char in enumerate(s):
            last_seen_idx[char] = i

            # find the minimum index among all three chars
            # this represents the rightmost position where we can start, and a substring ending at curr_idx that contains all three chars
            min_idx = min(last_seen_idx['a'], last_seen_idx['b'], last_seen_idx['c'])
            total_count+=min_idx+1
        return total_count
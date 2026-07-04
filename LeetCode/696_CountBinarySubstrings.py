class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        idx = 0
        n = len(s)
        group_counts = []

        while idx < n:
            curr_count=1
            while idx+1<n and s[idx]==s[idx+1]:
                curr_count+=1
                idx+=1
            group_counts.append(curr_count)
            idx+=1
        res = 0
        for i in range(len(group_counts)):
            res+=min(group_counts[i], group_counts[i-1])
        return res
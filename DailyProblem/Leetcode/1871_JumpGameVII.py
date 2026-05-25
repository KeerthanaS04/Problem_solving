class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        prefix_sum = [0] * (n + 1)
        prefix_sum[1] = 1 # position 0 is reachable
        reachable = [True]+[False] * (n - 1)

        for i in range(1, n):
            if s[i]=='0':
                left = max(0, i - maxJump)
                right = i - minJump

                if left<=right:
                    count_reachable = prefix_sum[right + 1] - prefix_sum[left]
                    reachable[i] = count_reachable > 0
            prefix_sum[i + 1] = prefix_sum[i] + (1 if reachable[i] else 0)
        return reachable[-1]
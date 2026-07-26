class Solution:
    def levelSort(self, arr):
        n = len(arr)
        ans = []
        level_size = 1
        idx = 0

        while idx < n:
            level = []
            for _ in range(level_size):
                if idx>=n:
                    break
                level.append(arr[idx])
                idx += 1

            level.sort()
            ans.append(level)
            level_size *= 2

        return ans
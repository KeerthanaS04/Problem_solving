class Solution:
    def countMinOperations(self, arr):
        total_increments = 0
        max_doubles = 0

        for num in arr:
            if num == 0:
                continue

            while num > 0:
                if num&1:
                    total_increments+=1
                if num>1:
                    curr_doubles+=1
                num>>=1
            max_doubles = max(max_doubles, curr_doubles)
        return total_increments + max_doubles
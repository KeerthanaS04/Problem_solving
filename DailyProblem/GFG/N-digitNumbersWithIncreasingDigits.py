from itertools import combination

class Solution:
    def increasingNumbers(self, n):
        if n == 1:
            return list(range(10))
        
        if n>9:
            return []
        
        ans = []
        for comb in combination('123456789', n):
            ans.append(''.join(comb))
        return ans
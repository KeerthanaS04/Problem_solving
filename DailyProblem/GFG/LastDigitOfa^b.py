class Solution:
    def getLastDigit(self, a, b):
        if b=='0':
            return 1
        
        cycle = [
            [0],
            [1],
            [2,4,8,6],
            [3,9,7,1],
            [4,6],
            [5],
            [6],
            [7,9,3,1],
            [8,4,2,6],
            [9,1]
        ]
        d = int(a[-1])
        c = cycle[d]
        length = len(c)
        rem = 0

        for ch in b:
            rem = (rem*10 + int(ch)) % length
        
        if rem == 0:
            rem = length
        return c[rem-1]
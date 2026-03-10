class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        mx = n-1
        left = -1
        right = -1

        for i in range(n-2, -1, -1):
            if s[i]>s[mx]:
                mx = i
            elif s[i]<s[mx]:
                left = i
                right = mx
        
        if left!=-1:
            s[left], s[right] = s[right], s[left]
        return int(''.join(s))
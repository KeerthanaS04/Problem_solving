class Solution:
    def processStr(self, s: str, k: int) -> str:
        m = 0
        for c in s:
            if c=='*':
                m = max(0, m-1)
            elif c=='#':
                m<<=1
            elif c!='%':
                m+=1
        if k>=m:
            return '.'
        
        for c in reversed(s):
            if c=='*':
                m+=1
            elif c=='#':
                m>>=1
                if k>=m: # finding out in which half of the string we are
                    k-=m
            elif c=='%':
                k = m-k+1
            else:
                m-=1
                if k==m:
                    return c
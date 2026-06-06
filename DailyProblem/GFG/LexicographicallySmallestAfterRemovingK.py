class Solution:
    def lexicographicallySmallest(self, s, k):
        n = len(s)

        # check n is power of 2
        if (n&(n-1))==0:
            k//=2
        else:
            k*=2
        
        if k>=n:
            return '-1'
        
        ans = []
        for ch in s:
            while ans and ans[-1]>ch and k>0:
                ans.pop()
                k-=1
            ans.append(ch)
        
        while k>0 and ans:
            ans.pop()
            k-=1
        res = ''.join(ans)
        return res if res else '-1'
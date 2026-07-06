class Solution:
    def maxPathSum(self, a, b):
        m = len(a)
        n = len(b)
        s1 = s2 = 0
        i = j = 0
        ans = 0

        while i < m and j < n:
            if a[i]==b[j]:
                ans += max(s1, s2) + a[i]
                s1 = s2 = 0
                i += 1
                j += 1
            elif a[i] < b[j]:
                s1 += a[i]
                i += 1
            else:
                s2 += b[j]
                j += 1
        
        while i < m:
            s1 += a[i]
            i += 1
        
        while j < n:
            s2 += b[j]
            j += 1
        
        ans+= max(s1, s2)
        return ans
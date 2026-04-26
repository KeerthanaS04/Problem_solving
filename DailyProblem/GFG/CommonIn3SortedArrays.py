from collections import Counter

class Solution:
    def commonElements(self, a, b, c):
        i = j = k = 0
        n1, n2, n3 = len(a), len(b), len(c)
        res = []

        while i<n1 and j<n2 and k<n3:
            if a[i]==b[i]==c[i]:
                # avoid duplicates
                if not res or res[-1]!=a[i]:
                    res.append(a[i])
                i+=1
                j+=1
                k+=1
            elif a[i]<b[j]:
                i+=1
            elif b[j]<c[k]:
                j+=1
            else:
                k+=1
        return res
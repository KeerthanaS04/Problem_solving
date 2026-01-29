from collections import deque
class Solution:
    def firstNonRepeating(self, s):
        nrc = deque()
        used = [0]*26
        ans = []

        for c in s:
            index = ord(c)-ord('a')
            
            if used[index]<1:
                nrc.append(c)
            used[index]+=1

            while nrc and used[ord(nrc[0])-ord('a')]>1:
                nrc.popleft()
            
            # append the result
            if not nrc:
                ans.append('#')
            else:
                ans.append(nrc[0])
        return ''.join(ans)
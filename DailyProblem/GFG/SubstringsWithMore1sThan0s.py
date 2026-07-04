from collections import defaultdict
class Solution:
    def countSubstring(self, s):
        ans = 0
        curr = 0
        prefix = 0
        mp = defaultdict(int)
        mp[0] = 1

        for ch in s:
            if ch=='0':
                prefix-=1
            else:
                prefix+=1
            
            if ch=='0':
                curr-=mp[prefix]
            else:
                curr+=mp[prefix-1]
            ans+=curr
            mp[prefix]+=1
        return ans
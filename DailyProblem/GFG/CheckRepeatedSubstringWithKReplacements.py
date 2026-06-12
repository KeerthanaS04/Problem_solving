from collections import defaultdict
class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        n = len(s)
        if n==k:
            return True
        
        mp = defaultdict(int)

        # count frequency of each substring of length k
        for i in range(0,n,k):
            new_str = s[i:i+k]
            mp[new_str] += 1
        
        # find the substring with maximum occurrence
        cnt_occurence = float("-inf")
        new_string = ""

        for key, value in mp.items():
            if value > cnt_occurence:
                cnt_occurence = value
                new_string = key
        
        # count how many blocks differ from the chosen substring
        i = 0
        convert = 0
        while i < n:
            x = i
            for j in range(k):
                if new_string[j] != s[x]:
                    convert += 1
                    break
                x += 1
            i += k
        return convert==0 or convert==1
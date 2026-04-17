from collections import Counter
class Solution:
    def canFormPalindrome(self, s):
        freq = Counter(s)
        odd_cnt = 0

        for count in freq.values():
            if count%2!=0:
                odd_cnt+=1
            if odd_cnt>1:
                return False
        return True
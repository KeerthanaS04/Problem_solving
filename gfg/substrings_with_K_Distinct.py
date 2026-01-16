class Solution:
    def countSubstr(self, s, k):
        def atmost_k(k):
            if k==0:
                return 0

            left = 0
            count = 0
            freq = [0]*26
            distinct = 0

            for right in range(len(s)):
                char_index = ord(s[right])-ord('a')

                if freq[char_index]==0:
                    distinct+=1
                freq[char_index]+=1

                while distinct>k:
                    left_char_index = ord(s[left]) - ord('a')
                    freq[left_char_index]-=1
                    if freq[left_char_index]==0:
                        distinct-=1
                    left+=1
                count += right-left+1
            return count
        return atmost_k(k)-atmost_k(k-1)
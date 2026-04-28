class Solution:
    def smallestSubstring(self, s):
        n = len(s)
        count = {'0':0, '1':0, '2':0}
        left = 0
        min_length = float('inf')

        for right in range(n):
            count[s[right]]+=1

            # check if window has all the three characters
            while count['0']>0 and count['1']>0 and count['2']>0:
                min_length = min(min_length, right-left+1)

                count[s[left]]-=1
                left+=1
        return min_length if n!=float('inf') else -1
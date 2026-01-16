from collections import defaultdict

class Solution:
    def countAtMostK(self, arr, k):
        if k==0:
            return 0
        
        left = 0
        count = 0
        freq = defaultdict(int)
        distinct = 0

        for right in range(len(arr)):
            if freq[arr[right]]==0:
                distinct+=1
            freq[arr[right]]+=1

            while distinct>k:
                freq[arr[left]]-=1

                if freq[arr[left]]==0:
                    distinct-=1
                left+=1
            count += right-left+1
        return count
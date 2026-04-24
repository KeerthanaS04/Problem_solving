class Solution:
    def visibleBuildings(self, arr):
        if not arr:
            return 0
        
        count = 1
        max_height = arr[0]

        for i in range(1, len(arr)):
            if arr[i]>=max_height:
                count+=1
                max_height = arr[i]
        return count
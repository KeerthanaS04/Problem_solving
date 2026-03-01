class Solution:
    def findClosestPair(self, arr1, arr2, x):
        n = len(arr1)
        m = len(arr2)
        start = 0
        end = m-1
        ele1 = float('-inf')
        ele2 = float('-inf')
        closestdiff = float('inf')

        while start<n and end>=0:
            sum = arr1[start]+arr2[end]
            absdiff = abs(sum-x)

            if absdiff<closestdiff:
                closestdiff = absdiff
                ele1 = arr1[start]
                ele2 = arr2[end]

            if sum>x:
                end-=1
            else:
                start+=1
        return [ele1, ele2]
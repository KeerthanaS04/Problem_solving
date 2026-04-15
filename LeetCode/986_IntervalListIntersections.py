from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []

        while i<len(firstList) and j<len(secondList):
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]

            intersect_start = max(s1, s2)
            intersect_end = min(e1, e2)

            if intersect_start<=intersect_end:
                res.append([intersect_start, intersect_end])
            
            # move the pointer of the interval that ends first
            if e1<e2:
                i+=1
            else:
                j+=1
        return res
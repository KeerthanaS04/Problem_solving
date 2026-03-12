from collections import defaultdict
from math import gcd
from typing import List
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        lookup_slope = defaultdict(int)
        lookup_line = defaultdict(int)
        lookup_slope_length = defaultdict(int)
        lookup_line_length = defaultdict(int)

        result = 0
        same = 0
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]

                dx = x2-x1
                dy = y2-y1
                g = gcd(dx, dy)
                a = dx//g
                b = dy//g

                if a<0 or (a==0 and b<0):
                    a = -a
                    b = -b
                c = b*x1-a*y1
                slope_key = (a,b)
                line_key = (a,b,c)
                result+=lookup_slope[slope_key]
                result-=lookup_line[line_key]

                lookup_slope[slope_key]+=1
                lookup_line[line_key]+=1

                l = dx*dx+dy*dy
                slope_len_key = (a,b,l)
                line_len_key = (a,b,c,l)
                same+=lookup_slope_length[slope_len_key]
                same-=lookup_line_length[line_len_key]

                lookup_slope_length[slope_len_key]+=1
                lookup_line_length[line_len_key]+=1
        return result-same//2
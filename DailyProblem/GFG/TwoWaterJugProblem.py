from math import gcd

class Solution:
    def minSteps(self, m, n, d):
        if d>max(m, n) or d%gcd(m,n)!=0:
            return -1
        if d==0:
            return 0
        
        def pour(a, b):
            count = 0
            x,y = 0, 0 # current water in jug a and jug b
            while x!=d and y!=d: # repeat conditions until we get d litres
                if x==0:
                    x = a # if a jug is empty, fill it
                    count+=1
                elif y==b: # if jug is full, empty it
                    y = 0
                    count+=1
                else: # otherwise pour from A->B
                    pour_amount = min(x, b-y)
                    x-=pour_amount
                    y+=pour_amount
                    count+=1
            return count
        return min(pour(m,n), pour(n,m))
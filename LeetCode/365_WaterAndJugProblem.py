from math import gcd
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target>x+y:
            return False
        if target==0:
            return True
        
        # check Bezout condition
        return target%gcd(x, y)==0
class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(x):
            y = 0

            while x>0:
                v = x%10
                y = y*10+v
                x//=10
            return y
        return abs(n-reverse(n))
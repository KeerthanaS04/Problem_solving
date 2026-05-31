class Solution:
    def countCollisions(self, directions: str) -> int:
        # remove non-colliding cars
        s = directions.lstrip('L').rstrip('R')
        return len(s)-s.count('S')
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def calculate_dist(dir1: str, dir2: str) -> int:
            max_dist = 0
            curr_dist = 0
            other_moves_count = 0

            for direction in s:
                if direction == dir1 or direction == dir2:
                    curr_dist += 1
                elif other_moves_count < k:
                    other_moves_count += 1
                    curr_dist+=1
                else:
                    curr_dist-=1
                max_dist = max(max_dist, curr_dist)
            return max_dist
        
        se = calculate_dist('S', 'E')
        sw = calculate_dist('S', 'W')
        ne = calculate_dist('N', 'E')
        nw = calculate_dist('N', 'W')

        return max(se, sw, ne, nw)
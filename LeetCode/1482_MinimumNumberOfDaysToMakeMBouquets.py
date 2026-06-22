from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def feasible(days: int) -> bool:
            bouquets_made = 0
            consecutive_bloomed = 0

            for bloom_day in bloomDay:
                if bloom_day <= days:
                    consecutive_bloomed += 1

                    if consecutive_bloomed == k:
                        bouquets_made += 1
                        consecutive_bloomed = 0
                else:
                    consecutive_bloomed = 0

            return bouquets_made >= m

        l, r = min(bloomDay), max(bloomDay)
        first_true_idx = -1

        while l <= r:
            mid = (l + r) // 2

            if feasible(mid):
                first_true_idx = mid
                r = mid - 1
            else:
                l = mid + 1

        return first_true_idx
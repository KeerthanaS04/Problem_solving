from typing import List
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        used = [False]*n
        unplaced_count = len(fruits)

        for fruit_size in fruits:
            for idx, basket_capacity in enumerate(baskets):
                if basket_capacity>=fruit_size and not used[idx]:
                    used[idx] = True
                    unplaced_count-=1
                    # move to the next fruit
                    break
        return unplaced_count
from typing import List
from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = Counter()
        max_fruits = 0
        l = 0

        for r, fruit_type in enumerate(fruits):
            fruit_count[fruit_type]+=1

            while len(fruit_count)>2:
                left_fruit = fruits[l]
                fruit_count[left_fruit]-=1

                if fruit_count[left_fruit]==0:
                    del fruit_count[left_fruit]
                l+=1
            max_fruits = max(max_fruits, r-l+1)
        return max_fruits
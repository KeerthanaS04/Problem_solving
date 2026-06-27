from typing import List
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # let the numbers be x-1, x, x+1 => 3x=s => x=s//3
        middle_number, remainder = divmod(num, 3)
        if remainder!=0:
            return []
        return [middle_number-1, middle_number, middle_number+1]
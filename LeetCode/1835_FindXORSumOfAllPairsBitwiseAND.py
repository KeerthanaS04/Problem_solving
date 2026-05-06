from functools import reduce
from operator import xor
from typing import List
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor1 = reduce(xor, arr1)
        xor2 = reduce(xor, arr2)
        return xor1&xor2
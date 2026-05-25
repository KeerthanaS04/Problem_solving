from typing import List
class BinaryIndexedTree:
    # BIT (Fenwick Tree) implementation for efficient prefix sum queries and updates
    __slots__ = ['n', 'c']
    def __init__(self, n: int) -> None:
        self.n = n
        self.c = [0] * (n + 1)
    
    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s

class NumArray:
    def __init__(self, nums: List[int]):
        self.tree = BinaryIndexedTree(len(nums))
        for i, val in enumerate(nums, 1):
            self.tree.update(i, val)
    
    def update(self, index: int, val: int) -> None:
        curr_val = self.sumRange(index, index)
        self.tree.update(index + 1, val - curr_val)
    
    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(right + 1) - self.tree.query(left)
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTree(self, root: Optional[TreeNode], start: int) -> int:
        self.Target = start
        self.ans = 0
        
        def time(node):
            if not node:
                return 0
            
            l = time(node.left)
            r = time(node.right)

            if node.val==self.Target:
                self.ans = max(self.ans, abs(l), abs(r))
                return 1
            elif l<=0 and r<=0:
                return min(l, r)-1
            elif l>=1:
                self.ans = max(self.ans, abs(l-r))
                return l+1
            elif r>=1:
                self.ans = max(self.ans, abs(l-r))
                return r+1
        time(root)
        return self.ans
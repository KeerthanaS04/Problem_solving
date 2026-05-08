class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def isSame(self, T, S):
        if T is None and S is None:
            return True
        if T is None or S is None:
            return False
        
        if T.data!=S.data:
            return False
        return (self.isSame(T.left, S.left) and self.isSame(T.right, S.right))
    
    def isSubTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (self.isSame(root1, root2) or self.isSubTree(root1.left, root2) or self.isSubTree(root1.right, root2))
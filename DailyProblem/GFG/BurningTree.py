class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def minTime(self, root, target):
        self.Target = target
        self.ans = 0

        def time(node):
            if not node:
                return 0
            l = time(node.left) # distance from target node
            r = time(node.right) #height of the subtree

            if node.data == self.Target:
                self.ans = max(self.ans, abs(l), abs(r))
                return 1
            elif l<=0 and r<=0:
                return min(l, r)+1
            elif l>=1:
                self.ans = max(self.ans, abs(l-r))
                return l+1
            elif r>=1:
                self.ans = max(self.ans, abs(l-r))
                return r+1
        time(root)
        return self.ans
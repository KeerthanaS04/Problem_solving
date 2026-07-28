class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

class Solution:
    def constructBinaryTree(self, pre, preMirror):
        self.pos = {}
        for i, val in enumerate(preMirror):
            self.pos[val] = i
        
        self.preIndex = 0

        def build(l, r):
            if l > r:
                return None
            root = Node(pre[self.preIndex])
            self.preIndex += 1

            if l == r:
                return root

            idx = self.pos[pre[self.preIndex]]
            root.left = build(idx, r)
            root.right = build(l+1, idx - 1)
            return root
        return build(0, len(pre) - 1)
from collections import deque
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    def topView(self, root):
        ans = []
        if not root:
            return ans
        
        mp = {}
        q = deque([(root, 0)])

        while q:
            node, level = q.popleft()

            if level not in mp:
                mp[level] = node.data
            if node.left:
                q.append((node.left, level-1))
            if node.right:
                q.append((node.right, level+1))
        for key in sorted(mp.keys()):
            ans.append(mp[key])
        return ans
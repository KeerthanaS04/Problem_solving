from collections import defaultdict
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

class Solution:
    def verticalSum(self, root):
        self.mn = float('inf')
        self.mx = float('-inf')
        mp = defaultdict(int)

        def dfs(node, vLevel):
            if not node:
                return
            
            self.mn = min(self.mn, vLevel)
            self.mx = max(self.mx, vLevel)

            mp[vLevel]+=node.data
            dfs(node.left, vLevel-1)
            dfs(node.right, vLevel+1)
        dfs(root, 0)
        ans = []
        for i in range(self.mn, self.mx+1):
            if mp[i]:
                ans.append(mp[i])
        return ans
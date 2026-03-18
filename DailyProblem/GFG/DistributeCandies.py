class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def help(self, root, ans):
        if not root:
            return 0
        l = self.help(root.left, ans)
        r = self.help(root.right, ans)
        ans[0]+= abs(l)+abs(r)

        return root.data+l+r-1
    
    def distCandy(self, root):
        ans = [0]
        self.help(root, ans)
        return ans[0]
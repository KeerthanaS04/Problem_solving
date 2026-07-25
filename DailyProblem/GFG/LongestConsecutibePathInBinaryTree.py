class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def longestConsecutive(self, root):
        if not root:
            return -1

        ans = 1
        def dfs(root, length):
            nonlocal ans
            if not root:
                return

            ans = max(ans, length)
            if root.left:
                dfs(root.left, length + 1)
            else:
                dfs(root.left, 1)

            if root.right:
                dfs(root.right, length + 1)
            else:
                dfs(root.right, 1)

        dfs(root, 1)
        return ans if ans>1 else -1
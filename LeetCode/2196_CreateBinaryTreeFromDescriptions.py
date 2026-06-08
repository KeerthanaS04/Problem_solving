from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent_val, child_val, is_left in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            children.add(child_val)
        
        if is_left:
            nodes[parent_val].left = nodes[child_val]
        else:
            nodes[parent_val].right = nodes[child_val]
        
        # find root node: the only node that appears as parent but never as child. Get the difference b/w all nodes and child nodes
        root_val = (set(nodes.keys())-children).pop()
        return nodes[root_val]
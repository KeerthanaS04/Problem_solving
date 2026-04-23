class SegmentTreeNode:
    __slots__ = ['left', 'right', 'lazy_tag', 'is_covered']

    def __init__(self):
        self.left = None
        self.right = None
        self.lazy_tag = 0 # lazy propagation tag: 1 for add, -1 for remove, 0 for None
        self.is_covered = False

class DynamicSegmentTree:
    __slots__ = ['root']

    def __init__(self):
        self.root = SegmentTreeNode()
    
    def modify(self, query_left: int, query_right: int, operation: int, tree_left: int=1, tree_right: int=10**9, node: SegmentTreeNode=None) -> None:
        if node is None:
            node = self.root
        
        if tree_left>=query_left and tree_right<=query_right:
            if operation==1:
                node.lazy_tag = 1
                node.is_covered = True
            else:
                node.lazy_tag = -1
                node.is_covered = False
            return
        self._push_down(node)

        mid = (tree_left+tree_right)>>1
        if query_left<=mid:
            self.modify(query_left, query_right, operation, tree_left, mid, node.left)
        if query_right>mid:
            self.modify(query_left, query_right, operation, mid+1, tree_right, node.right)
        self._push_up(node)
    
    def query(self, query_left: int, query_right: int, tree_left: int=1, tree_right: int=10**9, node: SegmentTreeNode=None) -> bool:
        if node is None:
            node = self.root
        if tree_left>=query_left and tree_right<=query_right:
            return node.is_covered
        
        self._push_down(node)
        mid = (tree_left+tree_right)>>1
        res = True

        if query_left<=mid:
            self.query(query_left, query_right, tree_left, mid, node.left)
        if query_right>mid:
            self.modify(query_left, query_right, mid+1, tree_right, node.right)
        return res
    
    def _push_up(self, node: SegmentTreeNode) -> None:
        node.is_covered = bool(node.left and node.left.is_covered and node.right and node.right.is_covered)
    
    def _push_down(self, node: SegmentTreeNode) -> None:
        if node.left is None:
            node.left = SegmentTreeNode()
        if node.right is None:
            node.right = SegmentTreeNode()
        
        if node.lazy_tag:
            node.left.lazy_tag = node.right.lazy_tag = node.lazy_tag
            node.left.is_covered = (node.lazy_tag==1)
            node.right.is_covered = (node.lazy_tag==1)
            node.lazy_tag = 0

class RangeModule:
    def __init__(self):
        self.tree = DynamicSegmentTree()
    
    def addRange(self, left: int, right: int) -> None:
        self.tree.modify(left, right-1, 1)
    
    def queryRange(self, left: int, right: int) -> bool:
        return self.tree.query(left, right-1)
    
    def removeRange(self, left: int, right: int) -> None:
        return self.tree.modify(left, right-1, -1)
class Node:
    __slots__ = ('left', 'right', 'l', 'r', 'mid', 'v', 'add')

    def __init__(self, left_bound: int, right_bound: int):
        self.left = None
        self.right = None
        self.l = left_bound
        self.r = right_bound
        self.mid = (left_bound+right_bound)//2
        self.v = 0 # value stored in this node (count of covered integers)
        self.add = 0 # Lazy propagation flag (1 if entire range should be marked)

class SegmentTree:
    # dynamic segment tree for range updates and queries
    def __init__(self):
        self.root = Node(1, int(1e9)+1)
    
    def modify(self, left: int, right: int, value: int, node: Node = None) -> None:
        if node is None:
            node = self.root
        
        if left>right:
            return
        
        # push down lazy updates before going deeper
        self.pushdown(node)
        if left<=node.mid:
            self.modify(left, right, value, node.left)
        if right>node.mid:
            self.modify(left, right, value, node.right)
        
        self.pushup(node)
    
    def query(self, left: int, right: int, node: Node=None) -> int:
        if node is None:
            node = self.root
        if left>right:
            return 0
        if node.l>=left and node.r<=right:
            return node.v
        self.pushdown(node)
        res = 0
        if left<=node.mid:
            res+=self.query(left, right, node.left)
        if right>node.mid:
            res+=self.query(left, right, node.right)
        return res
    
    def pushup(self, node: Node) -> None:
        node.v = node.left.v+node.right.v
    
    def pushdown(self, node: Node) -> None:
        if node.left is None:
            node.left = Node(node.l, node.mid)
        if node.right is None:
            node.right = Node(node.mid+1, node.r)
        
        if node.add!=0:
            left_child, right_child = node.left, node.right

            left_child.add = node.add
            right_child.add = node.add

            left_child.v = left_child.r - left_child.l + 1
            right_child.v = right_child.r - right_child.l + 1

            node.add = 0

class CountIntervals:
    def __init__(self):
        self.tree = SegmentTree()
    
    def add(self, left: int, right: int) -> None:
        self.tree.modify(left, right, 1)
    
    def count(self) -> int:
        return self.tree.query(1, int(1e9))
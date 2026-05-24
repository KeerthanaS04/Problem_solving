from typing import Optional
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val=val
        self.neighbors=neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(curr_node: Optional['Node']) -> Optional['Node']:
            if curr_node is None:
                return None
            if curr_node in visited_to_cloned:
                return visited_to_cloned[curr_node]
            
            cloned_node = Node(curr_node.val)
            visited_to_cloned[curr_node]=cloned_node

            for neighbor in curr_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            return cloned_node
        visited_to_cloned = {}
        return dfs(node)
from collections import defaultdict
from typing import List
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        child = defaultdict(list)
        # build adjacency representation of the tree
        for node_id in range(1, len(parent)):
            parent_id = parent[node_id]
            child[parent_id].append(node_id)
        
        self.max_length = 0

        def dfs(curr_node: int) -> int:
            longest_chain = 0
            for child_node in child[curr_node]:
                child_chain_length = dfs(child_node)+1

                if s[curr_node]!=s[child_node]:
                    # connecting two branches (longest_chain+child_chain_length)
                    self.max_length = max(self.max_length, longest_chain+child_chain_length)
                    longest_chain = max(longest_chain, child_chain_length)
            return longest_chain
        dfs(0)
        return self.max_length+1
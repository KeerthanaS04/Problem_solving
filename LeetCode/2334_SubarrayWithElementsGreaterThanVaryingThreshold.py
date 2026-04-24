from typing import List
class Solution:
    def validSubarrays(self, nums: List[int], threshold: int) -> int:
        def find_root(node: int) -> int:
            if parent[node]!=node:
                parent_node = find_root(parent[node])
            return parent[node]
        
        def union_sets(node_a: int, node_b: int) -> None:
            root_a = find_root(node_a)
            root_b = find_root(node_b)

            if root_a==root_b:
                return
            
            # merge set a into b
            parent[root_a] = root_b
            component_size[root_b]+=component_size[root_a]
        array_length = len(nums)
        parent = list(range(array_length))
        component_size = [1]*array_length

        sorted_elements = sorted(zip(nums, range(array_length)), reverse=True)
        visited = [False]*array_length

        for val, i in sorted_elements:
            # merge with left neighbor if it has been visited
            if i>0 and visited[i-1]:
                union_sets(i, i-1)
            # merge with right neighbor if it has been visited
            if i<array_length and visited[i+1]:
                union_sets(i, i+1)
            
            curr_component_size = component_size[find_root(i)]
            if val>threshold//curr_component_size:
                return curr_component_size
            visited[i] = True
        return -1
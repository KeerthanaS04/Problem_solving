from typing import List
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        def find(node: int) -> int:
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]
        parent = list(range(n))
        res = []

        # process each friend request
        for person_u, person_v in requests:
            parent_u = find(person_u)
            parent_v = find(person_v)
            
            if parent_u==parent_v:
                res.append(True)
            else:
                # check if merging these groups would violate any restrictions
                is_valid = True
                for restricted_x, restricted_y in restrictions:
                    parent_x = find(restricted_x)
                    parent_y = find(restricted_y)

                    if (parent_u==parent_x and parent_v==parent_y) or (parent_u==parent_y and parent_v==parent_x):
                        is_valid = False
                        break
                res.append(is_valid)
                
                if is_valid:
                    parent[parent_u] = parent_v
        return res
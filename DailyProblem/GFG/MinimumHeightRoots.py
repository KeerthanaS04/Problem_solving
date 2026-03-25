from collections import deque
class Solution:
    def minHeightRoot(self, V, edges):
        if V==1:
            return [0]
        adjacency_list = [[] for _ in range(V)]
        node_degrees = [0]*V

        for node_a, node_b in edges:
            adjacency_list[node_a].append(node_b)
            adjacency_list[node_b].append(node_a)
            node_degrees[node_a]+=1
            node_degrees[node_b]+=1
        
        # Initialize queue with all leave nides (degree=1)
        leaves_queue = deque(node for node in range(V) if node_degrees[node]==1)
        remaining_nodes = []

        # remove leave nodes layer by layer until we reach the center
        while leaves_queue:
            remaining_nodes.clear()
            curr_size = len(leaves_queue)
            for _ in range(curr_size):
                leaf_node = leaves_queue.popleft()
                remaining_nodes.append(leaf_node)

                # update degrees of neighbor and add new leaves to queue
                for neighbor in adjacency_list[leaf_node]:
                    node_degrees[neighbor]-=1
                    if node_degrees[neighbor]==1:
                        leaves_queue.append(neighbor)
        return remaining_nodes
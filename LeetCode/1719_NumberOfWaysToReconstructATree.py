from typing import List
from collections import defaultdict
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # create adjacency matrix to track connections b/w nodes
        adjacency_matrix = [[False]*510 for _ in range(510)]

        # create adjacency list to store neighbors for each node
        adjacency_list = defaultdict(list)

        # build the graph from the given pairs
        for node1, node2 in pairs:
            adjacency_matrix[node1][node2] = adjacency_matrix[node2][node1] = True
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)
        
        # collect all nodes that appear in the pairs
        active_nodes = []
        for node_id in range(510):
            if adjacency_list[node_id]:
                active_nodes.append(node_id)
                # mark self-connection as true for active nodes
                adjacency_matrix[node_id][node_id]=True
        
        # sort nodes by their degree (number of connections) in ascending order
        active_nodes.sort(key=lambda node: len(adjacency_list[node]))

        # track if there are multiple valid trees possible
        multiple_solutions_exist = False

        # count potential root nodes
        root_count = 0

        # check each node to find its potential parent in the tree
        for curr_idx, curr_node in enumerate(active_nodes):
            # look for the first node with higher or equal degree that is connected
            parent_idx = curr_idx+1
            while parent_idx < len(active_nodes) and not adjacency_matrix[curr_node][active_nodes[parent_idx]]:
                parent_idx += 1
            
            if parent_idx<len(active_nodes):
                # found a potential parent, check if it is the root
                parent_node = active_nodes[parent_idx]

                # check if degrees are equal (multiple valid parent choices)
                if len(adjacency_list[curr_node])==len(adjacency_list[parent_node]):
                    multiple_solutions_exist = True
                
                # verify that all neighbors of the potential parent are connected
                # this is necessary for a valid tree
                for neighbor in adjacency_list[curr_node]:
                    if not adjacency_matrix[parent_node][neighbor]:
                        return 0
            else:
                # no potential parent found, count this as a root
                root_count += 1
        # a valid tree exists if there are multiple valid root nodes
        if root_count>1:
            return 0
        return 2 if multiple_solutions_exist else 1
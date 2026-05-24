from typing import List
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        max_score = 0
        edge_scores = [0]*len(edges)

        for source_node, target_node in enumerate(edges):
            edge_scores[target_node]+=source_node

            # if curr_node has higher score, or same score but smaller idx
            if (edge_scores[max_score]<edge_scores[target_node] or 
                (edge_scores[max_score]==edge_scores[target_node] and target_node<max_score)):
                max_score=target_node
        return max_score
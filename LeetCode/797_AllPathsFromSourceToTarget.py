from collections import deque
class Solution:
    def allPathSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)

        # initialize queue with the starting path containing only node 0
        queue = deque([[0]])
        # store all valid paths from source to target
        res = []

        # BFS
        while queue:
            # get the current path from the queue
            curr_path = queue.popleft()

            # get the last node in the curr path
            last_node = curr_path[-1]
            # check if we've reached the last node
            if last_node==n-1:
                res.append(curr_path)
                continue

            # explore all neighbors of the curr node
            for neighbor in graph[last_node]:
                # create a new path by extending the curr_path with the neighbor
                new_path = curr_path+[neighbor]
                queue.append(new_path)
        return res
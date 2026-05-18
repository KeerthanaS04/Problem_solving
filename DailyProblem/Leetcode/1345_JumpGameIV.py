from typing import List
from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        val_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            val_to_indices[val].append(i)
        
        queue = deque([0])
        visited = {0}
        steps = 0

        # bfs to find minimum steps to reach the last idx
        while True:
            for _ in range(len(queue)):
                curr_idx = queue.popleft()

                if curr_idx==len(arr)-1:
                    return steps
                
                # move one step forward, backward, jump to any idx with the same value
                next_indices = [curr_idx+1, curr_idx-1]
                same_val_indices = val_to_indices.pop(arr[curr_idx], [])

                for next_idx in (*next_indices, *same_val_indices):
                    if 0<=next_idx<len(arr) and next_idx not in visited:
                        queue.append(next_idx)
                        visited.add(next_idx)
            steps+=1
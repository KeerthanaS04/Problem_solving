from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city_idx: int) -> None:
            visited[city_idx] = True

            for neighbor_idx, is_connected in enumerate(isConnected[city_idx]):
                if not visited[neighbor_idx] and is_connected:
                    dfs(neighbor_idx)
        n = len(isConnected)
        visited = [False]*n
        count = 0

        for city_idx in range(n):
            if not visited[city_idx]:
                dfs(city_idx)
                count+=1
        return count
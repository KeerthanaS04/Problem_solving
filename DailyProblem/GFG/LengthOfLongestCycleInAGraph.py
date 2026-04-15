class Solution:
    def longestCycle(self, V, edges):
        out = [-1]*V

        for u, v in edges:
            out[u] = V
        visited = [0]*V
        ans = -1

        for i in range(V):
            if visited[i]:
                continue
            step_map = {}
            node = i
            step = 0

            while node!=-1 and not visited[node]:
                visited[node]=1
                step_map[node]=step
                step+=1

                node = out[node]

                if node!=-1 and node in step_map:
                    cycle_length = step-step_map[node]
                    ans = max(ans, cycle_length)
                    break
        return ans
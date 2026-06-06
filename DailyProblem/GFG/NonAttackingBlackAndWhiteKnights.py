class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]
        ans = 0

        for i in range(n):
            for j in range(m):
                count = 1
                for d in range(8):
                    ni = i+dx[d]
                    nj = j+dy[d]

                    if 0<=ni<n and 0<=nj<m:
                        count += 1
                ans+=(n*m)-count
        return ans
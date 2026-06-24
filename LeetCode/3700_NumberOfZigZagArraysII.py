class Solution:
    MOD = 1_000_000_007
    def mat_mul(self, A, B):
        n = len(A)
        m = len(B[0])
        k = len(B)
        C = [[0]*m for _ in range(n)]

        for i in range(n):
            for t in range(k):
                if A[i][t]:
                    a = A[i][t]
                    for j in range(m):
                        C[i][j] = (C[i][j]+a*B[t][j])%self.MOD
        return C
    
    def mat_pow(self, M, p):
        n = len(M)
        res = [[0]*n for _ in range(n)]
        for i in range(n):
            res[i][i] = 1
        
        while p:
            if p&1:
                res = self.mat_mul(res, M)
            M = self.mat_mul(M, M)
            p >>= 1
        return res
    
    def mat_vec_mul(self, M, v):
        n = len(M)
        res = [0]*n

        for i in range(n):
            s = 0
            for j in range(n):
                s = (s+M[i][j]*v[j])%self.MOD
            res[i] = s
        return res
    
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r-l+1
        if n==1:
            return m
        
        # prefix transform T1
        T1 = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(i):
                T1[i][j] = 1
        
        # suffix transform T2
        T2 = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(i+1, m):
                T2[i][j] = 1
        
        # two step transition
        A = self.mat_mul(T2, T1)
        dp = [1]*m
        steps = n-1
        pairs = steps//2

        if pairs:
            A_pow = self.mat_pow(A, pairs)
            dp = self.mat_vec_mul(A_pow, dp)
        
        if steps&1:
            dp = self.mat_vec_mul(T1, dp)
        
        ans = sum(dp)%self.MOD
        return ans*2%self.MOD
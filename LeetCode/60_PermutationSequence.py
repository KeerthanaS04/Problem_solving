class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        used = [False]*(n+1)

        for pos in range(n):
            factorial = 1

            # factorial of remaining positions
            for i in range(1, n-pos):
                factorial*=i
            
            for digit in range(1, n+1):
                if not used[digit]:
                    if k>factorial:
                        k-=factorial
                    else:
                        res.append(str(digit))
                        used[digit] = True
                        break
        return ''.join(res)
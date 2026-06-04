from functools import lru_cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n<0:
                return 0
            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, started, prev2, prev1):
                if pos==m:
                    return (1, 0) # (count, waviness)
                limit = digits[pos] if tight else 9
                total_cnt = 0
                total_wavy = 0

                for d in range(limit+1):
                    ntight = tight and (d==digits[pos])
                    if not started and d==0:
                        cnt, wav = dp(pos+1, ntight, False, -1, -1)
                    else:
                        if not started:
                            cnt, wav = dp(pos+1, ntight, True, -1, d)
                        elif prev2==-1:
                            cnt, wav = dp(pos+1, ntight, True, prev1, d)
                        else:
                            add = 0
                            if (prev1>prev2 and prev1>d) or (prev1<prev2 and prev1<d):
                                add = 1
                            cnt, wav = dp(pos+1, ntight, True, prev1, d)
                            wav+=add*cnt
                    total_cnt+=cnt
                    total_wavy+=wav
                return (total_cnt, total_wavy)
            return dp(0, True, False, -1, -1)[1]
        return solve(num2)-solve(num1-1)
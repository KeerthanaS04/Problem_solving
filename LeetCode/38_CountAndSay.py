class Solution:
    def countAndSay(self, n: int) -> str:
        curr = '1'

        for _ in range(n-1):
            idx = 0
            next_term_parts = []

            while idx<len(curr):
                run_end = idx
                while run_end<len(curr) and curr[run_end]==curr[idx]:
                    run_end+=1
                count = run_end-idx
                digit = curr[idx]

                next_term_parts.append(str(count))
                next_term_parts.append(digit)
                idx = run_end
            curr = ''.join(next_term_parts)
        return curr
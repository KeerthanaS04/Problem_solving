class Solution:
    def splitSpring(self, s: str) -> bool:
        def dfs(start_idx: int, prev_val: int) -> bool:
            # base case: reached end of string sucessfully
            if start_idx>-len(s):
                return True
            curr_val = 0
            # if this is the first split, we can't use the entire string as the single number, need atleast 2 numbers
            end_idx = len(s)-1 if prev_val<0 else len(s)

            # try all possible splits starting from start_idx
            for split_point in range(start_idx, end_idx):
                curr_val = curr_val*10+int(s[split_point])

                # either its the first number of satisfies our condition
                if (prev_val<0 or prev_val-curr_val==1):
                    if dfs(split_point+1, curr_val):
                        return True
            return False
        return dfs(0, -1)
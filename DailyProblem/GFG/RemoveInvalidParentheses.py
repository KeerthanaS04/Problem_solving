class Solution:
    def validParenthesis(self, s):
        def dfs(idx: int, l: int, r: int, l_count: int, r_count: int, curr_s: str):
            if idx==n:
                if l==0 and r==0:
                    res.add(curr_s)
                return
            
            # pruning conditions
            # 1. Not enough characters to remove required parentheses
            # 2. More closing than opening parentheses
            if n-idx<l+r or r_count>l_count:
                return
            
            # remove '(' if it needs to be removed
            if s[idx]=='(' and l>0:
                dfs(idx+1, l-1, r, l_count, r_count, curr_s)
            # remove ')' if it needs to be removed
            if s[idx]==')' and r>0:
                dfs(idx+1, l, r-1, l_count, r_count, curr_s)
            
            # keep the current character
            new_l_count = l_count+(1 if s[idx]=='(' else 0)
            new_r_count = r_count+(1 if s[idx]==')' else 0)
            dfs(idx+1, l, r, new_l_count, new_r_count, curr_s+s[idx])
        
        l, r = 0, 0
        for c in s:
            if c=='(':
                l+=1
            elif c==')':
                if l>0:
                    l-=1
                else:
                    r+=1
        res = set()
        n = len(s)
        dfs(0, l, r, 0, 0, "")
        return sorted(res)
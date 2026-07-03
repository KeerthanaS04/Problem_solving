class Solution:
    def magicalString(self, n: int) -> int:
        if n==0:
            return 0
        
        magical_str = [1, 2, 2]
        grp_cnt_idx = 2

        while len(magical_str)<n:
            prev_ele = magical_str[-1]
            curr_ele = 3-prev_ele
            repeat_cnt = magical_str[grp_cnt_idx]
            magical_str.extend([curr_ele]*repeat_cnt)
            grp_cnt_idx += 1
        return magical_str[:n].count(1)
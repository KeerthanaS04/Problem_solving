class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        total_length = len(s)
        dash_count = s.count('-')
        char_count = total_length-dash_count

        first_grp_size = char_count%k
        if first_grp_size==0:
            first_grp_size = k
        res = []
        curr_grp_cnt = first_grp_size

        for i, c in enumerate(s):
            if c=='-':
                continue
            res.append(c.upper())
            curr_grp_cnt-=1

            if curr_grp_cnt==0:
                # reset counter for next group
                curr_grp_cnt = k
                if i!=total_length-1:
                    res.append('-')
        return ''.join(res).rstrip('-')
class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(len(s)-1):
            curr_val = ord(s[i])
            next_val = ord(s[i+1])

            # check if both digits have same parity (both odd or both even)
            if (curr_val+next_val)%2==0:
                if curr_val>next_val:
                    return s[:i]+s[i+1]+s[i]+s[i+2:]
        return s
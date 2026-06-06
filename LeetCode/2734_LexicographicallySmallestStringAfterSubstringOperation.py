class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)

        # find the first non-'a' character
        start_idx = 0
        while start_idx<n and s[start_idx]=="a":
            start_idx+=1
        
        # if all characters are 'a', change the last one to 'z'
        if start_idx==n:
            return s[:-1]+"z"
        
        # find the end of the continuous non-'a' substring
        end_idx = start_idx
        while end_idx<n and s[end_idx]!="a":
            end_idx+=1
        
        # decrease each character in the substring by 1
        modified_substring = ''.join(chr(ord(s[char])-1) for char in s[start_idx:end_idx])
        res = s[:start_idx]+modified_substring+s[end_idx:]
        return res
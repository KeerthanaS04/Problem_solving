class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        n = len(s)
        curr_index = 0

        while curr_index<n:
            next_index = curr_index
            while next_index<n and s[next_index]==s[curr_index]:
                next_index+=1
            consecutive_count = next_index-curr_index

            # keep only the remainder groups
            remainder = consecutive_count%k

            # check if we can merge or not
            if stack and stack[-1][0]==s[curr_index]:
                # merge with previous occurence
                stack[-1][1] = (stack[-1][1]+remainder)%k
                if stack[-1][1]==0:
                    stack.pop()
            elif remainder>0:
                stack.append([s[curr_index], remainder])
            
            # move to the next character
            curr_index = next_index
        
        result = [char*count for char, count in stack]
        return (''.join(result))
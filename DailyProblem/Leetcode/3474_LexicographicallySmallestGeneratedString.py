class Solution:
    def isSame(self, word, str2, i, m):
        for j in range(m):
            if word[i]!=str2[j]:
                return False
            i+=1
        return True
    
    def generateStringe(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        N = n+m-1
        word = ['$']*N
        canChange = [False]*N

        # Process 'T'
        for i in range(n):
            if str1[i]=='T':
                i_ = i
                for j in range(m):
                    if word[i_]!='$' and word[i_]!=str2[j]:
                        return ''
                    word[i_] = str2[j]
                    i_+=1
        
        # fill remaining with 'a'
        for i in range(n):
            if str1[i]=='F':
                if self.isSame(word, str2, i, m):
                    changed = False
                    for k in range(i+m-1, i-1, -1):
                        if canChange[k]:
                            word[k] = 'b'
                            changed = True
                            break
                    if not changed:
                        return ''
        return ''.join(word)
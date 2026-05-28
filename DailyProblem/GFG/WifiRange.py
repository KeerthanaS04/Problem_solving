class Solution:
    def wifiRange(self, s, x):
        n = len(s)
        freq = [0]*(n+1)

        for i in range(n):
            if s[i]=='1':
                left = max(i-x, 0)
                right = min(i+x, n-1)

                freq[left]+=1
                if right+1<n:
                    freq[right+1]-=1
        
        # prefix sum to coverage
        for i in range(n):
            if i>0:
                freq[i]+=freq[i-1]
            
            # no wi-fi coverage at this position
            if freq[i]==0:
                return False
        return True
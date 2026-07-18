class Solution:
    def sumScores(self, s: str) -> int:
        # Z-algorithm
        # calculate the z values and add the length of the string to the sum of all z values
        n = len(s)
        z = [0]*n
        l, r = 0, 0

        for i in range(1, n):
            if i<=r:
                z[i] = min(z[i-l], r-i+1)
            
            while i+z[i]<n and s[z[i]]==s[i+z[i]]:
                z[i] += 1
            
            if i+z[i]-1>r:
                l, r = i, i+z[i]-1
        return sum(z)+n
class Solution:
    def permute(self, arr):
        ans = []
        self.solve(0, arr, ans)
        return ans
    
    def solve(self, i, arr, ans):
        n = len(arr)
        if i==n:
            ans.append(arr[:])
            return
        
        for j in range(i, n):
            arr[i], arr[j] = arr[j], arr[i]
            self.solve(i+1, arr, ans)
            arr[i], arr[j] = arr[j], arr[i]
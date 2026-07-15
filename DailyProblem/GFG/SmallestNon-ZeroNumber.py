class Solution:
    def find(self, arr):
        # if x>a => x = x+(x-a) => 2x-a
        # if x<=a => x = x-(a-x) => 2x-a
        # need = 2x-a => x = (need+a)//2
        need = 0

        for i in range(len(arr)-1,-1,-1):
            need = (need+arr[i])//2
        return need
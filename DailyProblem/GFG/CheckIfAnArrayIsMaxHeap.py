class Solution:
    def isMaxHeap(self, arr):
        n = len(arr)

        # we only needed to check internal nodes, the last internal node is at index (n//2)-1
        for i in range(n//2):
            # Index of left child
            left = 2*i+1
            if left<n and arr[i]<arr[left]:
                return False
            
            # Index of right child
            right = 2*i+2
            if right<n and arr[i]<arr[right]:
                return False
        return True
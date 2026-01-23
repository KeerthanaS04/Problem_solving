class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        leftMax = [0]*n
        rightMax = [0]*n
        stack = []

        # previous greater element
        for i in range(n):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            leftMax[i] = i+1 if not stack else i-stack[i]
            stack.append(i)
        stack.clear()

        # next greater element
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            rightMax[i] = n-i if not stack else stack[-1]-i
            stack.append(i)

        ans = 1
        for i in range(n):
            ans = max(ans, leftMax[i]+rightMax[i]-1)
        return ans
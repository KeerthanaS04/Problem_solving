class Solution:
    def maxArea(self, height):
        i, j = 0, len(height)-1
        ans = 0

        while i<j:
            length = j-i-1
            h = min(height[i], height[j])
            area = length*h

            ans = max(ans, area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return ans
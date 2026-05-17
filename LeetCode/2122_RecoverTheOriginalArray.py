from typing import List
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        # try different possible values of 2k by pairing nums[0] with each other element
        for i in range(1, n):
            difference = nums[i]-nums[0]

            # skip invalid cases: difference must be positive and even
            if difference==0 or difference%2==1:
                continue
            visited = [False]*n
            visited[i] = True

            res = [(nums[0]+nums[i])>>1]
            l = 1
            r = i+1

            while r<n:
                # skip already visited elements on the left
                while l<n and visited[l]:
                    l+=1
                # find the matching element on the right with exact difference
                while r<n and nums[r]-nums[l]<difference:
                    r+=1
                # if no valid pair found, this k value won't work
                if r==n or nums[r]-nums[l]>difference:
                    break
                # mark the right element as used and add the original val to res
                visited[r] = 1
                res.append((nums[l]+nums[r])>>1)
                l+=1
                r+=1
            # if we successfully paired all elements, return the result
            if len(res)==(n>>1):
                return res
        return []
from collections import defaultdict, deque
from typing import List
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(list)
        max_ele = 0
        for i, num in enumerate(nums):
            mp[num].append(i)
            max_ele = max(max_ele, num)
        
        # build sieve
        is_prime = [True]*(max_ele+1)
        if max_ele>=0:
            is_prime[0] = False
        if max_ele>=1:
            is_prime[1] = False
        
        num = 2
        while num*num<=max_ele:
            if is_prime[num]:
                multiple = num*num
                while multiple<=max_ele:
                    is_prime[multiple] = False
                    multiple+=num
            num+=1
        
        # BFS
        q = deque([0])
        visited = [False]*n
        visited[0] = True
        seen = set()
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i==n-1:
                    return steps
                
                # i-1 -> left
                if i-1>=0 and not visited[i-1]:
                    visited[i-1] = True
                    q.append(i-1)
                
                # i+1 -> right
                if i+1<n and not visited[i+1]:
                    visited[i+1] = True
                    q.append(i+1)
                
                # skip if not prime or are already processed
                if not is_prime[nums[i]] or nums[i] in seen:
                    continue

                # visit all multiples
                multiple = nums[i]
                while multiple<=max_ele:
                    if multiple in mp:
                        for j in mp[multiple]:
                            if not visited[j]:
                                visited[j] = True
                                q.append(j)
                    multiple+=nums[i]
                seen.add(nums[i])
            steps+=1
        return -1
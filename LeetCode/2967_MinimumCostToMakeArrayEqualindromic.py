from bisect import bisect_left
from typing import List

palindromes = []
for i in range(1, 10**5+1):
    num_str = str(i)

    # create odd-length palindrome
    odd_palindrome = num_str+num_str[::-1]
    # create even-length palindrom
    even_palindrome = num_str+num_str[:-1][::-1]

    palindromes.append(int(odd_palindrome))
    palindromes.append(int(even_palindrome))

palindromes.sort()

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def calculate_total_diff(target: int) -> int:
            return sum(abs(num-target) for num in nums)
        nums.sort()
        median = nums[len(nums)//2]
        closest_idx = bisect_left(palindromes, median)
        min_cost = float('inf')
        for j in range(closest_idx-1, closest_idx+1):
            if 0<=j<len(palindromes):
                min_cost = min(min_cost, calculate_total_diff(palindromes[j]))
        return min_cost
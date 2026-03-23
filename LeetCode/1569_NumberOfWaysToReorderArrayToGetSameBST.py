from typing import List
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def count_bst_permutation(arr):
            if len(arr)<2:
                return 1
            root = arr[0]
            left_subtree = [x for x in arr if x<root]
            right_subtree = [x for x in arr if x>root]

            left_size = len(left_subtree)
            right_size = len(right_subtree)
            left_permutations = count_bst_permutation(left_subtree)
            right_permutations = count_bst_permutation(right_subtree)
            total_size = left_size+right_size
            combinations = binomial_coefficients[total_size][left_size]

            result = (combinations*left_permutations%MOD)*right_permutations%MOD
            return result
        MOD = 10**9+7
        n = len(nums)
        binomial_coefficients = [[0]*n for _ in range(n)]
        binomial_coefficients[0][0] = 1

        for i in range(1,n):
            binomial_coefficients[i][0] = 1
            for j in range(1, i+1):
                # c(i,j) = c(i-1, j)+c(i-1, j-1) = pascal's triangle
                binomial_coefficients[i][j] = (
                    binomial_coefficients[i-1][j]+binomial_coefficients[i-1][j-1]
                )%MOD
        total_permutations = count_bst_permutation(nums)
        return (total_permutations-1+MOD)%MOD
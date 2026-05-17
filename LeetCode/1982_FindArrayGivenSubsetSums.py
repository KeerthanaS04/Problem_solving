from typing import List
from sortedcontainers import SortedList
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        # the sum of all negative elements
        negative_sum = -min(sums)
        sorted_sums = SortedList(subset_sum+negative_sum for subset_sum in sums)
        sorted_sums.remove(0)

        # the smallest remaining sum must be one of the original array elements
        res = [sorted_sums[0]]

        for ele_idx in range(1,n):
            # remove all the subset sums that include the elements found so far
            for subset_mask in range(1<<ele_idx):
                # check if the subset includes the most recently found element
                if subset_mask>>(ele_idx-1)&1:
                    subset_sum = sum(res[bit_pos] for bit_pos in range(ele_idx) if subset_mask>>bit_pos&1)
                    sorted_sums.remove(subset_sum)
            # after removal the smallest sum is the next element
            res.append(sorted_sums[0])
        
        # determine which ele should be negative
        for sign_mask in range(1<<n):
            curr_sum = sum(res[bit_pos] for bit_pos in range(n) if sign_mask>>bit_pos&1)

            # if this combination gives us the original negative sum
            if curr_sum==negative_sum:
                # apply negative sign to selected elements
                for bit_pos in range(n):
                    if sign_mask>>bit_pos&1:
                        res[bit_pos]*=-1
                break
        return res
from typing import List
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def nxt_permutations(digits: List[str]) -> bool:
            n = len(digits)

            # find the rightmost digit that is smaller than its next digit
            pivot_idx = n-2
            while pivot_idx>=0 and digits[pivot_idx]>=digits[pivot_idx+1]:
                pivot_idx-=1
            
            # if no digit exist, this is the last permutation
            if pivot_idx<0:
                return False
            
            # find rightmost digit greater than pivot
            swap_idx = n-1
            while swap_idx>=0 and digits[swap_idx]<=digits[pivot_idx]:
                swap_idx-=1
            
            # swap pivot with the found digit
            digits[pivot_idx], digits[swap_idx] = digits[swap_idx], digits[pivot_idx]

            # reverse the suffix after pivot position
            digits[pivot_idx+1:] = digits[pivot_idx+1:][::-1]
            return True
        
        target_digits = list(num)

        # apply the nxt_permuatations k times to get the target configuration
        for _ in range(k):
            nxt_permutations(target_digits)
        
        # create bucket to store position of each digit (0-9)
        digit_positions = [[] for _ in range(10)]
        position_indices = [0]*10

        # populate position buckets for each digit in original string
        for pos, char in enumerate(target_digits):
            digit_val = ord(char)-ord('0')
            digit_positions[digit_val].append(pos)
        
        # map target digits to their corresponding positions in original string
        permutations_arr = [0]*len(num)
        for target_pos, char in enumerate(target_digits):
            digit_val = ord(char)-ord('0')
            original_pos = digit_positions[digit_val][position_indices[digit_val]]
            permutations_arr[target_pos] = original_pos
            position_indices[digit_val]+=1
        
        inversion_cnt = 0
        for i in range(len(num)):
            for j in range(i):
                if permutations_arr[j]>permutations_arr[i]:
                    inversion_cnt+=1
        return inversion_cnt
from typing import List
class Solution:
    def addOperator(self, num: str, target: int) -> List[str]:
        result = []

        def backtrack(idx: int, prev_operand: int, curr_eval: int, exp: str) -> None:
            # base case
            if idx==len(num):
                if curr_eval==target:
                    result.append(exp)
            
            # we will try all possible splits
            for i in range(idx, len(num)):
                # skip numbers with leading zeroes except single digit with 0
                if i!=idx and num[idx]=='0':
                    break
                curr_operand = int(num[idx:i+1])

                # first number in expression, no operand needed
                if idx==0:
                    backtrack(i+1, curr_operand, curr_operand, str(curr_operand))
                else:
                    # try addition
                    backtrack(i+1, curr_operand, curr_eval+curr_operand, exp+'+'+str(curr_operand))
                    # try subtraction
                    backtrack(i+1, -curr_operand, curr_eval-curr_operand, exp+'-'+str(curr_operand))
                    # try multiplication
                    backtrack(i+1, prev_operand*curr_operand, curr_eval-prev_operand+prev_operand*curr_operand, exp+'*'+str(curr_operand))
        backtrack(0, 0, 0, '')
        return result
from functools import cache
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def can_win(used_num_mask: int, curr_sum: int) -> bool:
            for num in range(1, maxChoosableInteger+1):
                # check if this number has been used
                if (used_num_mask>>num)&1==0:
                    new_sum = curr_sum+num

                    if new_sum>=desiredTotal:
                        return True

                    new_mask = used_num_mask|(1<<num)
                    if not can_win(new_mask, new_sum):
                        return True
            return False
        total_avail_sum = (1+maxChoosableInteger)*maxChoosableInteger//2
        if total_avail_sum<desiredTotal:
            return False
        return can_win(0, 0)
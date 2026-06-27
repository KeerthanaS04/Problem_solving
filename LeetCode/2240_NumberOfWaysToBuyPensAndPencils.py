class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        total_ways = 0
        max_pens = total//cost1
        for num_pens in range(max_pens+1):
            remaining_money = total-num_pens*cost1
            num_pencils_options = (remaining_money//cost2)+1
            total_ways += num_pencils_options
        return total_ways
from typing import List
import heapq
class Solution:
    def getNumberOfOrders(self, orders: List[int]) -> int:
        # initialize max heap for buyers and min heap for sellers
        buy_backlog = []
        sell_backlog = []

        for price, amount, order_type in orders:
            if order_type==0:
                while amount>0 and sell_backlog and sell_backlog[0][0]<=price:
                    sell_price, sell_amount = heapq.heappop(sell_backlog)

                    if amount>=sell_amount:
                        amount -= sell_amount
                    else:
                        # current buy order is partially consumed, push back the remaining sell order
                        heapq.heappush(sell_backlog, (sell_price, sell_amount-amount))
                        amount = 0
                # add remaining buy amount to backlog if any
                if amount>0:
                    heapq.heappush(buy_backlog, (-price, amount))
            else:
                while amount>0 and buy_backlog and buy_backlog[0][0]>=price:
                    buy_price, buy_amount = heapq.heappop(buy_backlog)

                    if amount>=buy_amount:
                        amount -= buy_amount
                    else:
                        # current sell order is partially consumed, push back the remaining buy order
                        heapq.heappush(buy_backlog, (buy_price, buy_amount-amount))
                        amount = 0
                # add remaining sell amount to backlog if any
                if amount>0:
                    heapq.heappush(sell_backlog, (price, amount))
        # calculate total backlog orders
        MOD = 10**9+7
        total_backlog = sum(order[1] for order in buy_backlog+sell_backlog)
        return total_backlog%MOD
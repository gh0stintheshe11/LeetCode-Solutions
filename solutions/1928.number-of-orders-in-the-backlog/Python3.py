from heapq import heappush, heappop
from typing import List

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10**9 + 7
        buy_heap = []  # max heap for buy orders (invert prices to use with min heap)
        sell_heap = []  # min heap for sell orders
        
        for price, amount, orderType in orders:
            if orderType == 0:  # buy order
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    sell_lowest_price, sell_amount = sell_heap[0]
                    if sell_amount <= amount:
                        amount -= sell_amount
                        heappop(sell_heap)
                    else:
                        sell_heap[0] = (sell_lowest_price, sell_amount - amount)
                        amount = 0
                if amount > 0:
                    heappush(buy_heap, (-price, amount))
            else:  # sell order
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    buy_highest_price, buy_amount = buy_heap[0]
                    if buy_amount <= amount:
                        amount -= buy_amount
                        heappop(buy_heap)
                    else:
                        buy_heap[0] = (buy_highest_price, buy_amount - amount)
                        amount = 0
                if amount > 0:
                    heappush(sell_heap, (price, amount))
        
        total_backlog = 0
        for _, amount in buy_heap:
            total_backlog += amount
        for _, amount in sell_heap:
            total_backlog += amount

        return total_backlog % MOD
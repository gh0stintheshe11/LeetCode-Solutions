class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7
        
        # Sort inventory in descending order
        inventory.sort(reverse=True)
        inventory.append(0)  # add a zero at the end to simplify logic
        
        def sum_range(start, end, cnt):
            return cnt * (start + end) * (start - end + 1) // 2
        
        max_profit = 0
        n = len(inventory)
        
        for i in range(n - 1):
            if orders == 0:
                break
            if inventory[i] > inventory[i + 1]:
                count = (i + 1) * (inventory[i] - inventory[i + 1])
                if orders >= count:
                    max_profit += sum_range(inventory[i], inventory[i + 1] + 1, i + 1)
                    orders -= count
                else:
                    full_rows = orders // (i + 1)
                    left_over = orders % (i + 1)
                    max_profit += sum_range(inventory[i], inventory[i] - full_rows + 1, i + 1)
                    max_profit += (inventory[i] - full_rows) * left_over
                    orders = 0
        
        return max_profit % MOD
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = -1
        max_rotations = -1
        current_profit = 0
        boarded_customers = 0
        waiting_customers = 0
        rotations = 0
        
        for new_customers in customers:
            waiting_customers += new_customers
            board_now = min(4, waiting_customers)
            waiting_customers -= board_now
            boarded_customers += board_now
            rotations += 1
            
            current_profit = boarded_customers * boardingCost - rotations * runningCost
            
            if current_profit > max_profit:
                max_profit = current_profit
                max_rotations = rotations
        
        while waiting_customers > 0:
            board_now = min(4, waiting_customers)
            waiting_customers -= board_now
            boarded_customers += board_now
            rotations += 1
            
            current_profit = boarded_customers * boardingCost - rotations * runningCost
            
            if current_profit > max_profit:
                max_profit = current_profit
                max_rotations = rotations
        
        return max_rotations if max_profit > 0 else -1
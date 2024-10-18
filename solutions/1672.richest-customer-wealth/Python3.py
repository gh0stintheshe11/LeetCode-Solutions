from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Initialize the maximum wealth to 0
        max_wealth = 0
        
        # Iterate over each customer's accounts
        for customer_accounts in accounts:
            # Calculate the wealth of the current customer
            current_wealth = sum(customer_accounts)
            # Update the maximum wealth if the current wealth is greater
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        
        return max_wealth
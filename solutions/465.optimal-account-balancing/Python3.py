from typing import List

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Step 1: Calculate net balance for each person
        balance = defaultdict(int)
        for frm, to, amount in transactions:
            balance[frm] -= amount
            balance[to] += amount
        
        # Filter out people with zero balance
        debt = list(filter(lambda x: x != 0, balance.values()))
        
        # Step 2: Backtracking to find the minimum number of transactions
        def dfs(start):
            # Skip settled debts
            while start < len(debt) and debt[start] == 0:
                start += 1
            if start == len(debt):
                return 0
            
            min_trans = float('inf')
            for i in range(start + 1, len(debt)):
                if debt[start] * debt[i] < 0:  # They can settle each other
                    # Try to settle debt[start] with debt[i]
                    debt[i] += debt[start]
                    min_trans = min(min_trans, 1 + dfs(start + 1))
                    # Backtrack
                    debt[i] -= debt[start]
            
            return min_trans
        
        return dfs(0)
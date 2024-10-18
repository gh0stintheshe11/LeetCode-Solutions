class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        # Precompute prefix sums for 'N' and suffix sums for 'Y'
        prefix_n = [0] * (n + 1)
        suffix_y = [0] * (n + 1)
        
        # Calculate prefix sums for 'N'
        for i in range(1, n + 1):
            prefix_n[i] = prefix_n[i - 1] + (1 if customers[i - 1] == 'N' else 0)
        
        # Calculate suffix sums for 'Y'
        for i in range(n - 1, -1, -1):
            suffix_y[i] = suffix_y[i + 1] + (1 if customers[i] == 'Y' else 0)
        
        # Find the minimum penalty and the earliest hour
        min_penalty = float('inf')
        best_time = 0
        
        for j in range(n + 1):
            penalty = prefix_n[j] + suffix_y[j]
            if penalty < min_penalty:
                min_penalty = penalty
                best_time = j
        
        return best_time
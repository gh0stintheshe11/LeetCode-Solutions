class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Calculate the base satisfaction (ignoring grumpy minutes)
        base_satisfaction = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        # Calculate the additional satisfaction using the secret technique in the first 'minutes' window
        additional_satisfaction = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)

        max_additional_satisfaction = additional_satisfaction

        # Slide the window over the rest of the array
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfaction += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfaction -= customers[i - minutes]
                
            max_additional_satisfaction = max(max_additional_satisfaction, additional_satisfaction)
        
        return base_satisfaction + max_additional_satisfaction
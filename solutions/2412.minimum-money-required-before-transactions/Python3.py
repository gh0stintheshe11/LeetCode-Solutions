class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        max_loss = 0
        required_start_amount = 0

        for cost, cashback in transactions:
            # Calculate the loss for each transaction and keep track of the max loss.
            required_start_amount += max(0, cost - cashback)
            # For all transactions update max loss to complete it
            max_loss = max(max_loss, min(cost, cashback))
        
        # The minimum money needed is total needed plus the greatest individual need.
        return required_start_amount + max_loss
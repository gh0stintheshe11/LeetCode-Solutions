class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        roundedAmount = (purchaseAmount + 5) // 10 * 10
        return 100 - roundedAmount
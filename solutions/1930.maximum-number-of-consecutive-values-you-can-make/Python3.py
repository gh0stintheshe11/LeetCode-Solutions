class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        max_consecutive = 0
        for coin in coins:
            if coin > max_consecutive + 1:
                break
            max_consecutive += coin
        return max_consecutive + 1
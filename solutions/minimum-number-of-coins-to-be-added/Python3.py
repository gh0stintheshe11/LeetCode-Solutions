class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        current_sum = 0
        additions = 0
        
        for coin in coins:
            while current_sum + 1 < coin and current_sum < target:
                current_sum += (current_sum + 1)
                additions += 1
            current_sum += coin
            if current_sum >= target:
                return additions
        
        while current_sum < target:
            current_sum += (current_sum + 1)
            additions += 1
        
        return additions
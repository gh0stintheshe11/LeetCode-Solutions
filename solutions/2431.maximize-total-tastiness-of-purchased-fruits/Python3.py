class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        n = len(price)
        dp = [[[-1] * (maxAmount + 1) for _ in range(maxCoupons + 1)] for _ in range(n + 1)]
        
        def dfs(idx, coupons, budget):
            if idx >= n or coupons < 0 or budget < 0:
                return 0
            if dp[idx][coupons][budget] != -1:
                return dp[idx][coupons][budget]
            
            # Option 1: Skip the current fruit
            option1 = dfs(idx + 1, coupons, budget)
                
            # Option 2: Buy the current fruit without a coupon (if affordable)
            option2 = 0
            if budget >= price[idx]:
                option2 = tastiness[idx] + dfs(idx + 1, coupons, budget - price[idx])
                
            # Option 3: Buy the current fruit with a coupon (if affordable and have coupons left)
            option3 = 0
            if coupons > 0 and budget >= price[idx] // 2:
                option3 = tastiness[idx] + dfs(idx + 1, coupons - 1, budget - price[idx] // 2)
            
            dp[idx][coupons][budget] = max(option1, option2, option3)
            return dp[idx][coupons][budget]
        
        return dfs(0, maxCoupons, maxAmount)
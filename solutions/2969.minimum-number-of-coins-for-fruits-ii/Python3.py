class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        que = collections.deque()

        for i in range(len(prices)):
            while que and que[0] < (i - 2) / 2:
                que.popleft()
            
            pre = dp[que[0]] if que else 0
            dp[i] = pre + prices[i]
            
            while que and dp[que[-1]] >= dp[i]:
                que.pop()
            que.append(i)

        return min(dp[ceil((len(prices) - 2) / 2) :])
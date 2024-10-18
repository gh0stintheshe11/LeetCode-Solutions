class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def dp(cur_id, not_free): 
            if cur_id == len(prices):
                return 0
            # not buy
            notbuy = float('inf')
            if not_free > cur_id:
                notbuy = dp(cur_id+1, not_free)
            # buy
            buy = dp(cur_id+1, min(2*cur_id+2, len(prices))) + prices[cur_id]
            return min(notbuy, buy)        
        return dp(0, 0)
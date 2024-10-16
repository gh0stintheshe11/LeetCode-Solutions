
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @cache
        def dp(cur_needs: tuple) -> int:
            cost = sum(n * price[i] for i, n in enumerate(cur_needs)) 
            for offer in special:
                new_needs = [cur_needs[i] - offer[i] for i in range(len(needs))]
                if min(new_needs) < 0: continue
                cost = min(cost, offer[-1] + dp(tuple(new_needs)))
            return cost
        return dp(tuple(needs))

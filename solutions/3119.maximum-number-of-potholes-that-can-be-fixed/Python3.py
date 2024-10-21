class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        potGrps = sorted(map(len, road.split('.')), reverse=True)
        ans = 0

        for pots in potGrps:
            if budget == 0 or pots == 0: 
                return ans

            potsFixed = min(budget - 1, pots)
            budget -= potsFixed + 1
            ans += potsFixed

        return ans
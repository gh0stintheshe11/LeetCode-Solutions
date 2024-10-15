from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        def canUpgrade(ct, upCost, sellPrice, availMoney, numToUpgrade):
            totalCost = numToUpgrade * upCost
            availableMoney = availMoney + (ct - numToUpgrade) * sellPrice
            return availableMoney >= totalCost

        result = []
        for i in range(len(count)):
            low, high = 0, count[i]
            while low < high:
                mid = (low + high + 1) // 2
                if canUpgrade(count[i], upgrade[i], sell[i], money[i], mid):
                    low = mid
                else:
                    high = mid - 1
            result.append(low)
        return result
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        dp0 = 0  # max is 1<<sum(rewardValues)
        dp0 |= 1 << 0
        for x in rewardValues: 
            dp1 = dp0 & ((1 << x) - 1)  # only consider scores > x
            dp1 <<= x  # add x to all values in bitset. 
            dp0 |= dp1  # merge bitsets
        return dp0.bit_length() - 1
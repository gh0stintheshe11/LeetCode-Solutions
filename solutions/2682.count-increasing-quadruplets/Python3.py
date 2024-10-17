class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        contador = 0

        for j in range(len(nums)):
            prv = 0

            for i in range(j):
                if nums[j] > nums[i]:
                    prv = prv + 1
                    contador = contador + dp[i]
                elif nums[j] < nums[i]:
                    dp[i] = dp[i] + prv

        return contador
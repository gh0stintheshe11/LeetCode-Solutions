class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        stack = []
        for i, x in enumerate(nums): 
            while stack and stack[-1][1] <= x: 
                ii, xx = stack.pop()
                if xx == x:
                    dp[i] = dp[ii]+1
                    break 
            stack.append((i, x))
        return sum(dp)
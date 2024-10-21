class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        if nums[0] == 0 and len(set(nums)) == 1: return [0 for a in queries]
        n = len(nums)
        dp = [[[0,0] for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = [nums[i],nums[i]]
        for d in range(1,n):
            for i in range(n-d):
                j = i+d
                d1,m1 = dp[i][j-1]
                d2,m2 = dp[i+1][j]
                dd = d1^d2
                m = max(m1,m2,dd)
                dp[i][j] = [dd,m]

        return [dp[i][j][1] for i,j in queries]
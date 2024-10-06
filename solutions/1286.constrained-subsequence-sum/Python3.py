from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = nums[:]
        dq = deque()
        
        max_sum = nums[0]
        
        for i in range(n):
            if dq and dq[0] < i - k:
                dq.popleft()
            
            if dq:
                dp[i] = max(dp[i], dp[dq[0]] + nums[i])
            
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
                
            dq.append(i)
            
            max_sum = max(max_sum, dp[i])
        
        return max_sum
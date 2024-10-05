from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # This will store the smallest tail of all increasing subsequences
        # with length i+1 in dp[i].
        dp = []
        
        for num in nums:
            # Find the index of the smallest number in dp which is greater than or equal to num
            idx = bisect_left(dp, num)
            
            # If num is larger than any element in dp, append it
            if idx == len(dp):
                dp.append(num)
            else:
                # Otherwise, replace the first element in dp which is greater than or equal to num
                dp[idx] = num
        
        # The length of dp will be our answer
        return len(dp)
from typing import List

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        mod = 10**9 + 7
        n = len(nums)
        pow2 = [1] * n
        
        for i in range(1, n):
            pow2[i] = pow2[i-1] * 2 % mod
        
        result = 0
        for i in range(n):
            result = (result + nums[i] * (pow2[i] - pow2[n-1-i])) % mod
        
        return result
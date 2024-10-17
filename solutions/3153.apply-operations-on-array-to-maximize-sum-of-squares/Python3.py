from typing import List
from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        
        d = defaultdict(int)
        
        for i in range(N):
            s = bin(nums[i])[2:]
            
            r = 0
            
            for i in range(len(s) - 1, -1, -1):
                if s[i] == "1":
                    d[2 ** r] += 1
                    
                r += 1

        ans = 0
        for _ in range(k):
            num = 0
            for key in list(d.keys()):
                
                num += key
                d[key] -= 1
                
                
                if d[key] == 0:
                    del d[key]

            ans += num ** 2
            ans %= MOD

        return ans % MOD
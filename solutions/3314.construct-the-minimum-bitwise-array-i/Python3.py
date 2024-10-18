from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            found = False
            # Check possible ans[i] from 0 to num-1
            for a in range(num):
                if a | (a + 1) == num:
                    ans.append(a)
                    found = True
                    break
            if not found:
                ans.append(-1)
                
        return ans
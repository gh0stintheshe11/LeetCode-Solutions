from typing import List
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        
        t, q = SortedList(), SortedList()
        ans = float("inf")
        i = 1
        j = 2
        s = nums[0]
        
        while i < n - k + 2:
            s += -nums[i - 1] + nums[i]
            
            if (-nums[i], i) in t:
                t.discard((-nums[i], i))
                s -= nums[i]
            else:
                q.discard((nums[i], i))
                
            while j < min(i + dist + 1, n):
                q.add((nums[j], j))
                j += 1
            
            while len(t) < k - 2:
                w, z = q.pop()
                t.add((-w, z))
                s += w
            
            while q and t and -t[0][0] > q[0][0]:
                w, z = t.pop(0)
                w0, z0 = q.pop(0)
                q.add((-w, z))
                t.add((-w0, z0))
                s += w + w0
                
            ans = min(ans, s)
            i += 1
        
        return ans + nums[0]
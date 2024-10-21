from typing import List
from collections import defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        appendfreq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
            
        for num in nums:
            if freq[num] == 0:
                continue
            elif appendfreq[num] > 0:
                appendfreq[num] -= 1
                appendfreq[num + 1] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                appendfreq[num + 3] += 1
            else:
                return False
            
            freq[num] -= 1
        
        return True
from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Step 1: Sort the envelopes
        # Sort by width in ascending order, and by height in descending order if widths are the same
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Step 2: Extract the heights and find the LIS
        heights = [envelope[1] for envelope in envelopes]
        
        # Function to find the length of LIS using binary search
        def length_of_LIS(nums):
            lis = []
            for num in nums:
                pos = bisect.bisect_left(lis, num)
                if pos == len(lis):
                    lis.append(num)
                else:
                    lis[pos] = num
            return len(lis)
        
        return length_of_LIS(heights)
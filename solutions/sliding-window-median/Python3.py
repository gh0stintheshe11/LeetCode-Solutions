from sortedcontainers import SortedList
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def get_median(window):
            n = len(window)
            if n % 2 == 1:
                return float(window[n // 2])
            else:
                return (window[n // 2 - 1] + window[n // 2]) / 2
        
        window = SortedList()
        medians = []
        
        for i in range(len(nums)):
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i - k])
            if len(window) == k:
                medians.append(get_median(window))
        
        return medians
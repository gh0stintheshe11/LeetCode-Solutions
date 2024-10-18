from collections import Counter
from bisect import bisect_left, insort

class Solution:
    def getSubarrayBeauty(self, nums, k, x):
        result = []
        negatives = []
        
        for i in range(len(nums)):
            if nums[i] < 0:
                insort(negatives, nums[i])
            
            if i >= k:
                if nums[i - k] < 0:
                    index = bisect_left(negatives, nums[i - k])
                    negatives.pop(index)
            
            if i >= k - 1:
                if len(negatives) < x:
                    result.append(0)
                else:
                    result.append(negatives[x - 1])
        
        return result
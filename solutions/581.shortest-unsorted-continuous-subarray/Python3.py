class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = -1, -1
        max_seen = float('-inf')
        min_seen = float('inf')
        
        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                end = i
        
        for i in range(n-1, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                start = i

        if start == -1 and end == -1:
            return 0
        
        return end - start + 1
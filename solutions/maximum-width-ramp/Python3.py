class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        candidates = [(num, i) for i, num in enumerate(nums)]
        candidates.sort()
        
        max_width = 0
        min_index = float('inf')
        
        for value, index in candidates:
            if index < min_index:
                min_index = index
            else:
                max_width = max(max_width, index - min_index)
        
        return max_width
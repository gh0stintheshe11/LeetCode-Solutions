class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        position = 0
        boundary_count = 0
        
        for num in nums:
            position += num
            if position == 0:
                boundary_count += 1
        
        return boundary_count
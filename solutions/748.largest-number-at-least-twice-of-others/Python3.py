class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        max_num = max(nums)
        max_index = nums.index(max_num)
        
        for num in nums:
            if num != max_num and max_num < 2 * num:
                return -1
        
        return max_index
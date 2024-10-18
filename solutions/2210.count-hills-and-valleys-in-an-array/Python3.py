class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)
        prev = nums[0]
        
        i = 1
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                i += 1
                continue
            
            if (prev < nums[i] > nums[i + 1]) or (prev > nums[i] < nums[i + 1]):
                count += 1
                prev = nums[i]
            
            i += 1
        
        return count
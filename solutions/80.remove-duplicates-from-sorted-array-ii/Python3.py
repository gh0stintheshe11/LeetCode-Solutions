class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 3: 
            return len(nums)

        pos = 1
        for i in range(1, len(nums) - 1):
            if nums[i-1] != nums[i+1]:
                nums[pos] = nums[i]
                pos += 1
        nums[pos] = nums[-1]
        return pos + 1
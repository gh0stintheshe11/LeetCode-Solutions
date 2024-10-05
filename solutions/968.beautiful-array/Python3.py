class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def helper(nums):
            if len(nums) <= 2:
                return nums
            return helper(nums[::2]) + helper(nums[1::2])
        
        return helper(list(range(1, n + 1)))
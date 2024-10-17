class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        s = nums[0] + nums[1]
        res = 0
        while len(nums) >= 2:
            if nums[0] + nums[1] == s:
                del nums[0]
                del nums[0]
                res += 1
            else:
                return res
        return res
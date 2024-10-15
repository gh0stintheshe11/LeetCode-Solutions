class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        conc_val = 0
        while len(nums) > 1:
            first = nums.pop(0)
            last = nums.pop()
            conc_val += int(str(first) + str(last))
        if nums:
            conc_val += nums[0]
        return conc_val
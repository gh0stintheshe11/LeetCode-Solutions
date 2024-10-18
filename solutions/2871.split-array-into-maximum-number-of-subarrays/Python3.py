class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        overall_and = nums[0]
        for num in nums:
            overall_and &= num
        if overall_and != 0:
            return 1

        count = 0
        current_and = ~0  # All bits set
        for num in nums:
            current_and &= num
            if current_and == 0:
                count += 1
                current_and = ~0
        return count
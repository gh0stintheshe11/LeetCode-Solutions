class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        inpnums = tuple(nums)

        @lru_cache
        def remove(nums, expectedScore):
            first, last, both = 0, 0, 0
            if len(nums) >= 2 and expectedScore == nums[0] + nums[1]:
                first = remove(nums[2:], expectedScore)
            if len(nums) >= 2 and expectedScore == nums[-2] + nums[-1]:
                last = remove(nums[:-2], expectedScore)
            if len(nums) >= 2 and expectedScore == nums[0] + nums[-1]:
                both = remove(nums[1:-1], expectedScore)

            return max(first, last, both) + 1

        return max(
            remove(inpnums[1:-1], inpnums[0] + inpnums[-1]),
            remove(inpnums[:-2], inpnums[-2] + inpnums[-1]),
            remove(inpnums[2:], inpnums[0] + inpnums[1]),
        )
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRobWithCapability(capability):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2  # skip adjacent house
                else:
                    i += 1
                if count >= k:
                    return True
            return False

        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if canRobWithCapability(mid):
                right = mid
            else:
                left = mid + 1
        return left
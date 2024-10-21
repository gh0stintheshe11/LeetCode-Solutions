class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        if nums[n // 2] == k:
            return ans
        elif nums[n // 2] < k:
            index = bisect_left(nums, k)
            for i in range(n//2, index):
                ans += k - nums[i]
        else:
            index = bisect_right(nums, k)
            for i in range(index, n//2 + 1):
                ans += nums[i] - k

        return ans
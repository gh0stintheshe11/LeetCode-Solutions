class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        # Calculate LIS from the left
        lis_left = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis_left[i] = max(lis_left[i], lis_left[j] + 1)

        # Calculate LIS from the right (equivalent to LIS from the left for reversed array)
        lis_right = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[j] < nums[i]:
                    lis_right[i] = max(lis_right[i], lis_right[j] + 1)

        # Find the maximum mountain we can have
        max_mountain = 0
        for i in range(1, n-1):
            if lis_left[i] > 1 and lis_right[i] > 1:  # Need at least one element on each side
                max_mountain = max(max_mountain, lis_left[i] + lis_right[i] - 1)

        # Minimum elements to remove to make the mountain array
        return n - max_mountain
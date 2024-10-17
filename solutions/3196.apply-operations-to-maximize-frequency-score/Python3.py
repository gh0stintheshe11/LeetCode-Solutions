class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        pref = [0] + list(accumulate(nums))
        ans = 0
        l = 0
        for r in range(1, N + 1):
            mid = (l + r) // 2
            median = nums[mid]
            cost = abs((r - mid) * median - (pref[r] - pref[mid]))
            cost += abs((mid - l) * median - (pref[mid] - pref[l]))
        
            if cost > k:
                l += 1

            ans = max(ans, r - l)

        return ans
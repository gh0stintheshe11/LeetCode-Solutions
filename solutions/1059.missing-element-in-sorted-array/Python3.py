class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing_count(index):
            return nums[index] - nums[0] - index
        
        n = len(nums)
        if k > missing_count(n - 1):
            return nums[-1] + k - missing_count(n - 1)
        
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if missing_count(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return nums[left - 1] + k - missing_count(left - 1)
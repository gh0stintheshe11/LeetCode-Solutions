class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if not nums:
            return False
        min_val = min(nums)
        max_val = max(nums)
        n = len(nums)
        if max_val - min_val + 1 != n:
            return False
        return len(set(nums)) == n
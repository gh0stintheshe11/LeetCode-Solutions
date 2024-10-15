class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_value = max(nums)
        return k * max_value + k * (k - 1) // 2
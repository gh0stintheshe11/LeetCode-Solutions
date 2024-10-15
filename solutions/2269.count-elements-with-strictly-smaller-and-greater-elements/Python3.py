class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        return sum(min_num < num < max_num for num in nums)
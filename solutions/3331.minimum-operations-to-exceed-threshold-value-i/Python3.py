class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(1 for num in nums if num < k)
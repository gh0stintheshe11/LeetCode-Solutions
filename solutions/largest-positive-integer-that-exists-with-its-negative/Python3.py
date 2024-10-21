class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_k = -1
        for num in nums:
            if -num in num_set:
                max_k = max(max_k, abs(num))
        return max_k
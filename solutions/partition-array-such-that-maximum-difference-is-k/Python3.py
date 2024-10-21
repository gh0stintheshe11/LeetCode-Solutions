class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        subsequences = 0
        start_index = 0
        for i in range(len(nums)):
            if nums[i] - nums[start_index] > k:
                subsequences += 1
                start_index = i
        return subsequences + 1
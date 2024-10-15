class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_to_index = {}
        current_sum = 0
        max_length = 0
        for i, num in enumerate(nums):
            current_sum += num
            if current_sum == k:
                max_length = i + 1
            if current_sum - k in sum_to_index:
                max_length = max(max_length, i - sum_to_index[current_sum - k])
            if current_sum not in sum_to_index:
                sum_to_index[current_sum] = i
        return max_length
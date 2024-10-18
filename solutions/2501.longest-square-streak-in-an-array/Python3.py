class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = -1

        for num in nums:
            current_streak = 0
            current_num = num

            while current_num in num_set:
                current_streak += 1
                current_num = current_num * current_num

            if current_streak >= 2:
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
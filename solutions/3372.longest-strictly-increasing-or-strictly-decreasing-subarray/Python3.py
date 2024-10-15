class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        max_length = 1
        cur_length_inc = 1
        cur_length_dec = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cur_length_inc += 1
                cur_length_dec = 1
            elif nums[i] < nums[i - 1]:
                cur_length_dec += 1
                cur_length_inc = 1
            else:
                cur_length_inc = 1
                cur_length_dec = 1

            max_length = max(max_length, cur_length_inc, cur_length_dec)

        return max_length
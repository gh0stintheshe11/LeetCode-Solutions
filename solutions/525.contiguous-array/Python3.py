class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        count_map = {0: -1}  # Initialize with count 0 at index -1

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in count_map:
                max_length = max(max_length, i - count_map[count])
            else:
                count_map[count] = i

        return max_length
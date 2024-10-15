class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        # Calculate max valid subsequence with same parity
        odd_count = sum(num % 2 != 0 for num in nums)
        even_count = len(nums) - odd_count
        
        # Calculate max valid subsequence with alternating parity
        max_alternating = max(self.maxAlternating(nums, 0), self.maxAlternating(nums, 1))
        
        # Return the max of these possibilities
        return max(max_alternating, odd_count, even_count)

    def maxAlternating(self, nums: list[int], expected_parity: int) -> int:
        length = 0
        for num in nums:
            if num % 2 == expected_parity:
                length += 1
                expected_parity = 1 - expected_parity
        return length
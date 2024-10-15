class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        power_of_two = 1 << k

        # Precompute the prefix and suffix OR arrays
        prefix_or = [0] * n
        suffix_or = [0] * n

        # Fill prefix OR array
        prefix_or[0] = 0
        for i in range(1, n):
            prefix_or[i] = prefix_or[i - 1] | nums[i - 1]

        # Fill suffix OR array
        suffix_or[n - 1] = 0
        for i in range(n - 2, -1, -1):
            suffix_or[i] = suffix_or[i + 1] | nums[i + 1]

        max_or_value = 0

        # Calculate maximum OR value by trying to apply all operations on each element
        for i in range(n):
            # OR(value after multiplication, prefix OR, suffix OR)
            current_value = (nums[i] * power_of_two)
            max_or_value = max(max_or_value, prefix_or[i] | current_value | suffix_or[i])
        
        return max_or_value
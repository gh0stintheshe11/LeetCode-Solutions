class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        result = 0
        # Iterate over bits from 0 to 30 (since nums[i] < 2^31)
        for bit in range(31):
            mask = 1 << bit
            count = 0
            # Count how many numbers in nums have the current bit set
            for num in nums:
                if num & mask:
                    count += 1
            # If count is at least k, set this bit in the result
            if count >= k:
                result |= mask
        return result
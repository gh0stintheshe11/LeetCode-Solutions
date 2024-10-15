class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_size = 0
        for bit_pos in range(24):  # Since candidates[i] <= 10^7, check up to 24 bits.
            count = 0
            for num in candidates:
                if num & (1 << bit_pos):
                    count += 1
            max_size = max(max_size, count)
        return max_size
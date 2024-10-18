class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones, max_zeros = 0, 0
        current_ones, current_zeros = 0, 0

        for char in s:
            if char == '1':
                current_ones += 1
                current_zeros = 0
            else:
                current_zeros += 1
                current_ones = 0
            
            max_ones = max(max_ones, current_ones)
            max_zeros = max(max_zeros, current_zeros)

        return max_ones > max_zeros
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        max_gap = 0
        prev_index = -1
        
        for i, bit in enumerate(binary):
            if bit == '1':
                if prev_index != -1:
                    max_gap = max(max_gap, i - prev_index)
                prev_index = i
                
        return max_gap
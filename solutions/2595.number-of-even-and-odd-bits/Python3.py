class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        bit_index = 0
        
        while n > 0:
            if n & 1:
                if bit_index % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n = n >> 1
            bit_index += 1
        
        return [even, odd]
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num_bits = bin(num2).count('1')
        result = 0

        # Use bits from num1 as much as possible
        for i in range(31, -1, -1):
            if num_bits == 0:
                break
            if (num1 & (1 << i)) != 0:
                result |= (1 << i)
                num_bits -= 1
        
        # If there are more bits to set, set the remaining ones from the least significant bits
        for i in range(31):
            if num_bits == 0:
                break
            if (result & (1 << i)) == 0:
                result |= (1 << i)
                num_bits -= 1
        
        return result
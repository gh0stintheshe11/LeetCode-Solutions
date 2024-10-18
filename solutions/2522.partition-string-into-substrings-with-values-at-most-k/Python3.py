class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        num_parts = 0
        current_value = 0
        
        for digit in s:
            digit_value = int(digit)
            
            if digit_value > k:
                return -1
            
            new_value = current_value * 10 + digit_value
            
            if new_value > k:
                num_parts += 1
                current_value = digit_value
            else:
                current_value = new_value
        
        return num_parts + 1
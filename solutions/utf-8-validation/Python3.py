from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_num_of_bytes(num: int) -> int:
            if num >> 7 == 0: return 1  # 1-byte char
            elif num >> 5 == 0b110: return 2  # 2-byte char
            elif num >> 4 == 0b1110: return 3  # 3-byte char
            elif num >> 3 == 0b11110: return 4  # 4-byte char
            else: return 0  # Invalid
            
        n = len(data)
        i = 0
        
        while i < n:
            num_bytes = get_num_of_bytes(data[i])
            if num_bytes == 0 or i + num_bytes > n:
                return False
            
            for j in range(1, num_bytes):
                if data[i + j] >> 6 != 0b10:
                    return False
                
            i += num_bytes
        
        return True
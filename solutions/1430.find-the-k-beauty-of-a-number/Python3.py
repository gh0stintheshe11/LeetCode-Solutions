class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        length = len(num_str)
        k_beauty_count = 0
        
        for i in range(length - k + 1):
            substring = num_str[i:i + k]
            value = int(substring)
            if value != 0 and num % value == 0:
                k_beauty_count += 1
        
        return k_beauty_count
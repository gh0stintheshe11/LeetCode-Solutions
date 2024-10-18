class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        n = len(s)
        max_unique = 26  # At most 26 different characters (a-z)
        result = 0
        
        for unique in range(1, max_unique + 1):
            target_length = unique * count
            if target_length > n:
                break
            
            char_count = [0] * 26
            distinct_chars = 0
            freq_count = 0
            
            for i in range(n):
                if i >= target_length:
                    left_char_index = ord(s[i - target_length]) - ord('a')
                    if char_count[left_char_index] == count:
                        freq_count -= 1
                    char_count[left_char_index] -= 1
                    if char_count[left_char_index] == 0:
                        distinct_chars -= 1
                
                current_char_index = ord(s[i]) - ord('a')
                if char_count[current_char_index] == 0:
                    distinct_chars += 1
                char_count[current_char_index] += 1
                if char_count[current_char_index] == count:
                    freq_count += 1
                
                if i >= target_length - 1 and distinct_chars == unique and freq_count == unique:
                    result += 1
        
        return result
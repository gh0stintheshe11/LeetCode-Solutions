class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        left = 0
        right = 0
        max_length = 0
        char_frequency = {}
        
        while right < len(s):
            char = s[right]
            char_frequency[char] = char_frequency.get(char, 0) + 1

            while len(char_frequency) > k:
                left_char = s[left]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length
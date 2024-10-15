class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        count = 0
        char_map = {}
        for i in range(len(s)):
            # Add current character to the map
            char_map[s[i]] = char_map.get(s[i], 0) + 1
            # Remove the character that is out of the sliding window
            if i >= k:
                char_map[s[i - k]] -= 1
                if char_map[s[i - k]] == 0:
                    del char_map[s[i - k]]
            # Check if the window size is k and all characters are unique
            if i >= k - 1 and len(char_map) == k:
                count += 1
        return count
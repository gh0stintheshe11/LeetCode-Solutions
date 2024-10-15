class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {}
        max_length = -1
        
        for index, char in enumerate(s):
            if char in first_occurrence:
                max_length = max(max_length, index - first_occurrence[char] - 1)
            else:
                first_occurrence[char] = index
        
        return max_length
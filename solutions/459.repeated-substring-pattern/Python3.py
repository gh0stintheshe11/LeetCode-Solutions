class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Concatenate the string with itself
        doubled_s = s + s
        # Remove the first and the last character
        new_s = doubled_s[1:-1]
        # Check if the original string is a substring of the modified concatenated string
        return s in new_s
class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set(s)
        for char in range(ord('Z'), ord('A') - 1, -1):
            if chr(char) in seen and chr(char + 32) in seen:
                return chr(char)
        return ""
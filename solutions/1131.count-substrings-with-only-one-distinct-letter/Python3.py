class Solution:
    def countLetters(self, s: str) -> int:
        count = 0
        length = 0
        for i in range(len(s)):
            if i == 0 or s[i] == s[i-1]:
                length += 1
            else:
                count += (length * (length + 1)) // 2
                length = 1
        count += (length * (length + 1)) // 2
        return count
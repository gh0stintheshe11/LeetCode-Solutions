class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = s.count(letter)
        return (count * 100) // len(s)
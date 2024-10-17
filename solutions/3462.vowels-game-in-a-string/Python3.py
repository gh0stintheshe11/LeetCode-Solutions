class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(i in "aeiou" for i in s)
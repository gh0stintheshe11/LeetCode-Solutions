class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        n = len(s) // 2
        count_first_half = sum(char in vowels for char in s[:n])
        count_second_half = sum(char in vowels for char in s[n:])
        return count_first_half == count_second_half
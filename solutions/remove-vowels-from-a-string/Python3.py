class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join([char for char in s if char not in 'aeiou'])
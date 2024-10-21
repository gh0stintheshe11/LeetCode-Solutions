class Solution:
    def countVowels(self, word: str) -> int:
        total_vowels = 0
        vowels = set('aeiou')
        n = len(word)

        for i, char in enumerate(word):
            if char in vowels:
                total_vowels += (i + 1) * (n - i)
                
        return total_vowels
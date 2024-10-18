class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False
        
        for char in word:
            if not (char.isdigit() or char.isalpha()):
                return False
            if char in vowels:
                has_vowel = True
            elif char.isalpha():
                has_consonant = True
        
        return has_vowel and has_consonant
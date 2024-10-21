class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        count = 0
        
        for start in range(n):
            current_vowels = set()
            for end in range(start, n):
                if word[end] not in vowels:
                    break
                current_vowels.add(word[end])
                if len(current_vowels) == 5:  # All vowels are present
                    count += 1
        
        return count
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowels_in_s = sorted([char for char in s if char in vowels])
        result = []
        vowel_index = 0
        
        for char in s:
            if char in vowels:
                result.append(vowels_in_s[vowel_index])
                vowel_index += 1
            else:
                result.append(char)
                
        return ''.join(result)
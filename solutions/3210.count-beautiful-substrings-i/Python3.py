class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        beautiful_count = 0
        n = len(s)
        
        for i in range(n):
            vowels = 0
            consonants = 0
            for j in range(i, n):
                if s[j] in vowels_set:
                    vowels += 1
                else:
                    consonants += 1
                
                if vowels == consonants and (vowels * consonants) % k == 0:
                    beautiful_count += 1
        
        return beautiful_count
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        retcnt = 0
        vow = ["a", "e", "i", "o", "u"]
        
        for i in range(len(word)):
            consonant = 0
            need = Counter()

            for j in range(i, len(word)):

                if word[j] in vow:
                    need[word[j]] += 1
                else:
                    consonant += 1
                
                if consonant == k and len(need) == 5:
                    retcnt += 1

                    
        return retcnt
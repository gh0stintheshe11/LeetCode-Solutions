from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        memo = {}

        def canForm(word):
            if word in memo:
                return memo[word]
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in word_set and (suffix in word_set or canForm(suffix)):
                    memo[word] = True
                    return True
            
            memo[word] = False
            return False
        
        result = []
        for word in words:
            if canForm(word):
                result.append(word)
                
        return result
from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word: str) -> str:
            return "".join('*' if c in 'aeiou' else c for c in word.lower())
        
        exact = set(wordlist)
        lowercase = {}
        devoweled = {}
        
        for word in wordlist:
            lower = word.lower()
            devow = devowel(word)
            if lower not in lowercase:
                lowercase[lower] = word
            if devow not in devoweled:
                devoweled[devow] = word
        
        result = []
        for query in queries:
            if query in exact:
                result.append(query)
            elif query.lower() in lowercase:
                result.append(lowercase[query.lower()])
            elif devowel(query) in devoweled:
                result.append(devoweled[devowel(query)])
            else:
                result.append("")
        
        return result